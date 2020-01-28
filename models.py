# -*- coding: utf-8 -*-

from datetime import timedelta
from odoo import models, fields, api, exceptions


class Book(models.Model):
    _name = 'library.book'

    name = fields.Char(string="Title", required=True)
    description = fields.Text()

    responsible_id = fields.Many2one('res.books',
        ondelete='set null', string="Responsible", index=True)
    session_ids = fields.One2many(
        'library.session', 'course_id', string="Sessions")

    _sql_constraints = [
        ('name_description_check',
         'CHECK(name != description)',
         "The title of the course should not be the description"),

        ('nameUnique',
         'UNIQUE(name)',
         "The course title must be unique"),
    ]

    @api.one
    def copy(self, default=None):
        default = dict(default or {})

        copied_count = self.search_count(
            [('name', '=like', u"Copy of {}%".format(self.name))])
        if not copied_count:
            new_name = u"Copy of {}".format(self.name)
        else:
            new_name = u"Copy of {} ({})".format(self.name, copied_count)

        default['name'] = new_name
        return super(Course, self).copy(default)

class Session(models.Model):
    _name = 'library.session'

    name = fields.Char(required=True)
    start_date = fields.Date(default=fields.Date.today)
    duration = fields.Float(digits=(6, 2), help="Duration in days")
    seats = fields.Integer(string="Number of seats")
    active = fields.Boolean(default=True)
    color = fields.Integer()

    bookseller_id = fields.Many2one('res.partner', string="Bookseller",
        domain=['|', ('bookseller', '=', True),
                     ('category_id.name', 'ilike', "Bookseller")])
    book_id = fields.Many2one('library.book',
        ondelete='cascade', string="Book", required=True)
    client_ids = fields.Many2many('res.partner', string="Clients")

    clients_count = fields.Integer(
        string="Clients count", compute='_get_clients_count', store=True)

    taken_books = fields.Float(string="Taken books", compute='_taken_books')

    end_date = fields.Date(string="End Date", store=True,
        compute='_get_end_date', inverse='_set_end_date')
    hours = fields.Float(string="Duration in hours",
                         compute='_get_hours', inverse='_set_hours')

    state = fields.Selection([
         ('taken', "Taken"),
         ('returned', "Returned"),
         ('done', "Done")
    ])

    @api.one
    def action_take(self):
        self.state = 'taken'

    @api.one
    def action_return(self):
        self.state = 'returned'

    @api.one
    @api.depends('books', 'client_ids')
    def _taken_books(self):
        if not self.books:
            self.taken_books = 0.0
        else:
            self.taken_books = 100.0 * len(self.client_ids) / self.books

    @api.onchange('books', 'client_ids')
    def _verify_valid_books(self):
        if self.books < 0:
            return {
                'warning': {
                    'title': "Incorrect 'books' value",
                    'message': "The number of available books may not be negative",
                },
            }
        if self.books < len(self.client_ids):
            return {
                'warning': {
                    'title': "Too many clients",
                    'message': "Increase books count",
                },
            }

    @api.one
    @api.depends('start_date', 'duration')
    def _get_end_date(self):
        if not (self.start_date and self.duration):
            self.end_date = self.start_date
            return

        # Add duration to start_date, but: Monday + 5 days = Saturday, so
        # subtract one second to get on Friday instead
        start = fields.Datetime.from_string(self.start_date)
        duration = timedelta(days=self.duration, seconds=-1)
        self.end_date = start + duration

    @api.one
    def _set_end_date(self):
        if not (self.start_date and self.end_date):
            return

        # Compute the difference between dates, but: Friday - Monday = 4 days,
        # so add one day to get 5 days instead
        start_date = fields.Datetime.from_string(self.start_date)
        end_date = fields.Datetime.from_string(self.end_date)
        self.duration = (end_date - start_date).days + 1

    @api.one
    @api.depends('duration')
    def _get_hours(self):
        self.hours = self.duration * 24

    @api.one
    def _set_hours(self):
        self.duration = self.hours / 24

    @api.one
    @api.depends('client_ids')
    def _get_attendees_count(self):
        self.attendees_count = len(self.attendee_ids)

    @api.one
    @api.constrains('bookseller_id', 'client_ids')
    def _check_bookseller_not_in_clients(self):
        if self.bookseller_id and self.bookseller_id in self.client_ids:
            raise exceptions.ValidationError("A bookseller cannot be a client")

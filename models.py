from odoo import models, fields, api
from datetime import timedelta

class Book(models.Model):
    _name = 'book.model'

    name = fields.Char(string="Nombre")
    description = fields.Text(string="Descripción")
    release_date = fields.Date(string="Fecha de publicación", store=True)
    genres = fields.Selection([('gen1', 'Fantasia'), ('gen2', 'Ciencia ficción'), ('gen3','Romance'), ('gen4','Aventura'), ('gen5','Misterio'), ('gen6', 'Distópica')], 'Género', default='gen1')
    start_date = fields.Date(string="Fecha de inicio", default=fields.Date.today)
    duration = fields.Float(string="Duración", digits=(6, 2), help="Duration in days") 
    end_date = fields.Date(string="Fecha de finalización", store=True, compute='_get_end_date', inverse='_set_end_date')

    @api.depends('start_date', 'duration')
    def _get_end_date(self):
        for r in self:
            if not (r.start_date and r.duration):
                r.end_date = r.start_date
                continue
            # Add duration to start_date, but: Monday + 5 days = Saturday, so
            # subtract one second to get on Friday instead
            duration = timedelta(days=r.duration, seconds=-1)
            r.end_date = r.start_date + duration

    def _set_end_date(self):
        for r in self:
            if not (r.start_date and r.end_date):
                continue
            r.duration = (r.end_date - r.start_date).days + 1

class Author(models.Model):
    _name = 'author.model'

    name = fields.Char(string="Nombre")
    surname = fields.Char(string="Apellido")
    birth_date = fields.Date(string="Fecha de nacimiento", store=True)


    
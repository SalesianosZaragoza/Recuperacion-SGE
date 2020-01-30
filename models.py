from datetime import timedelta, date, datetime
from odoo import models, fields, api, exceptions


class Author(models.Model):
    _name = 'author.model'
    _description = "Modulo de autores"
    _inherit = 'base.entidad'

    name = fields.Char(string="nombre", required=True)
    surname = fields.Char(string="Apellidos", required=True)
    book_id = fields.One2many('book.model', 'author_id', string="libro")
    birthDate = fields.Date('fecha de nacimiento')
    prize_id = fields.Many2many(
        'prize.model', 'author_prize', 'author_id', 'prize_id', 'premios')


class Book(models.Model):
    _name = 'book.model'
    _description = "Modulo de libros"
    _inherit = 'base.entidad'

    title = fields.Char(string="titulo", required=True)
    author_id = fields.Many2one('author.model', string='autor', required=True)
    publicationDate = fields.Date(string="Fecha de publicación")
    color = fields.Integer(string="color")
    gender = fields.Char(string="género", required = True)


class Prize(models.Model):
    _name = 'prize.model'
    _description = "Modulo de libros"
    _inherit = 'base.entidad'

    name = fields.Char(string="nombre", required=True)
    year = fields.Integer(string="Año")
    author_id = fields.Many2many(
        'author.model', 'author_prize', 'prize_id', 'author_id', 'autores')

    @api.constrains('year')
    def _check_year(self):
        now = default=datetime.now().year
        for record in self:
            if record.year > now:
                raise exceptions.ValidationError("El año no puede ser mayor al actual")

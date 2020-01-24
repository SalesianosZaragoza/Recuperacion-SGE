from odoo import models, fields, api, exceptions
from datetime import timedelta

class Book(models.Model):
    _name = 'book.model'

    name = fields.Char(string="Nombre")
    description = fields.Text(string="Descripción")
    release_date = fields.Date(string="Fecha de publicación", store=True)
    genres = fields.Selection([('gen1', 'Fantasia'), ('gen2', 'Ciencia ficción'), ('gen3','Romance'), ('gen4','Aventura'), ('gen5','Misterio'), ('gen6', 'Distópica')], 'Género', default='gen1')
    start_date = fields.Date(string="Fecha de recordatorio", default=fields.Date.today)


class Author(models.Model):
    _name = 'author.model'

    name = fields.Char(string="Nombre")
    surname = fields.Char(string="Apellido")
    birth_date = fields.Date(string="Fecha de nacimiento", store=True)
    age = fields.Integer('age')

    @api.constrains('age')
    def _check(self):
        if self.age < 18:
            raise exceptions.ValidationError("La edad no puede ser inferior a 18")

    _sql_constraints = [
        ('name_surname_check',
        'CHECK(name != surname)',
        "El nombre no puede ser el mismo que el del apellido")
    ]
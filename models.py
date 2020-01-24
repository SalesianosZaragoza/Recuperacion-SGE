from odoo import models, fields, api, exceptions
from datetime import timedelta

class Book(models.Model):
    _name = 'book.model'

    name = fields.Char(string="Nombre")
    description = fields.Text(string="Descripción")
    release_date = fields.Date(string="Fecha de publicación", store=True)
    genres = fields.Selection([('gen1', 'Fantasia'), ('gen2', 'Ciencia ficción'), ('gen3','Romance'), ('gen4','Aventura'), ('gen5','Misterio'), ('gen6', 'Distópica')], 'Género', default='gen1')
    start_date = fields.Date(string="Fecha de recordatorio", default=fields.Date.today)

    # Relational fields

    prizes_id = fields.Many2many('prize.model', string="Premios")

class Author(models.Model):
    _name = 'author.model'

    name = fields.Char(string="Nombre")
    surname = fields.Char(string="Apellido")
    birth_date = fields.Date(string="Fecha de nacimiento", store=True)
    age = fields.Integer('age')

    # Relational fields

    prize_id = fields.One2many('prize.model', 'author_id', string="Premios")


    # Model Constrains

    @api.constrains('age')
    def _check(self):
        if self.age < 18:
            raise exceptions.ValidationError("La edad no puede ser inferior a 18")

    _sql_constraints = [
        ('name_surname_check',
        'CHECK(name != surname)',
        "El nombre no puede ser el mismo que el del apellido")
    ]

class Prize(models.Model):
    _name = 'prize.model'

    typePrize = fields.Selection([('p1', 'Literatura'), ('p2', 'Man Book International'), ('p3','Miguel Cervantes'), ('p4','Goncourt'), ('p5','Franz Kafka')], 'Premios', default='p1')

    # Relational fields

    author_id = fields.Many2one('author.model', ondelete='cascade', string="Autor", required=True)

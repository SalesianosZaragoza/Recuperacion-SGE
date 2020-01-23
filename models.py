from odoo import models, fields

class Book(models.Model):
    _name = 'book.model'

    name = fields.Char(string="Nombre")
    description = fields.Text(string="Descripción")
    release_date = fields.Date(string="Fecha de publicación", store=True)
    genres = fields.Selection([('gen1', 'Fantasia'), ('gen2', 'Ciencia ficción'), ('gen3','Romance'), ('gen4','Aventura'), ('gen5','Misterio'), ('gen6', 'Distópica')], 'Género', default='gen1')

class Author(models.Model):
    _name = 'author.model'

    name = fields.Char(string="Nombre")
    surname = fields.Char(string="Apellido")
    birth_date = fields.Date(string="Fecha de nacimiento", store=True)
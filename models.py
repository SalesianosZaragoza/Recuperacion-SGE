from odoo import models, fields

class Book(models.Model):
    _name = 'book.model'

    name = fields.Char(string='Nombre', required=True)
    description = fields.Text(string='Descripción', size=300, required=True)
    release_date = fields.date(string="Fecha de salida", store=True, default=fields.date.today, required=True)
    genres = fields.Selection(['Fantasia', 'Ciencia ficción', 'Romance', 'Aventura', 'Misterio', 'Distópica'], required=True, default='Fantasia')
from odoo import models, fields, api, exceptions
from datetime import timedelta

class Author(models.Model):
	_name = 'author.model'

	name = fields.char(string ="Nombre")
	birthdate = fields.datetime(string = "Fecha de nacimiento")
	book_id = fields.Many2many('book.model' string="libros escritos por el autor: ")


class Book(models.Model):
	_name = 'book.model'

	name = fields.char(string = "Titulo del libro")
	author = fields.char(string = "autor del titulo")
	publication_date = fields.Date(string = "Fecha de publicacion", default = fields.Date.today)
	topic = fields.Selection([ ('type1', 'Type 1'),('type2', 'Type 2'),],'Type')
	author_id = fields.Many2many('author.model', string="escrito por:")
	start_date = fields.Date(string="Fecha de publicacion" , default = fields.Date.today)
	premios_id = fields.Many2many('awards.model', string="premiso ganados por el libro:")
	color = fields.Integer()
	


class Awards(models.Model):
	_name = 'awards.model'

	name = fields.char(string = "Premio")
	yearAward = fields.Date(string = "Año en que ganó el premio")
	authors_id = fields.Many2many('book.model' string=" libros ganadores:")
	







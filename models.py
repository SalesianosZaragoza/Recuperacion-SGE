from odoo import models, fields, api, exceptions
from datetime import timedelta

class Author(models.Model):
	_name = 'author_model'

	name = fields.char(string ="Nombre")
	birthdate = fields.datetime(string = "Fecha de nacimiento")


class Book(models.Model):
	_name = 'book_model'

	name = fields.char(string = "Titulo del libro")
	author = fields.char(string = "autor del titulo")
	publication_date = fields.Date(string = "Fecha de publicacion", default = fields.Date.today)
	topic = fields.Selection([ ('type1', 'Type 1'),('type2', 'Type 2'),],'Type', default='type1')


class Awards(models.Model):
	_name = 'awards_model'

	name = fields.char(string = "Premio")
	yearAward = fields.Date(string = "Año en que ganó el premio")
	







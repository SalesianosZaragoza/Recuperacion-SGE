from odoo import models, fields, api, exceptions
from datetime import timedelta

class Author(models.Model):
	_name = 'author.model'

	name = fields.char(string ="Nombre")
	birthdate = fields.datetime(string = "Fecha de nacimiento", store = True)
	book_id = fields.Many2many('book.model' string="libros escritos por el autor: ")

	@api.constrains('birthdate')
def _check_something(self):
    for record in self:
        if record.birthdate < 8
            raise ValidationError("Todavía no sabe limpiarse el culete, cómo va a poder escribir un libro: %s" % record.birthdate)


class Book(models.Model):
	_name = 'book.model'

	name = fields.char(string = "Titulo del libro")
	author = fields.char(string = "autor del titulo")
	publication_date = fields.Date(string = "Fecha de publicacion", default = fields.Date.today)
	topic = fields.Selection([ ('type1', 'Type 1'),('type2', 'Type 2'),],'Type')
	n_pages = fields.Integer(string = "numero de páginas")
	extension = fields.char(string="La extensión del libro es:", required = True)
	author_id = fields.Many2many('author.model', string="escrito por:")
	start_date = fields.Date(string="Fecha de publicacion" , default = fields.Date.today)
	premios_id = fields.Many2many('awards.model', string="premiso ganados por el libro:")
	color = fields.Integer()

	@api.onchange('n_pages')
    def _count_pages(self):
        if self.n_pages < 0:
            return {
                'warning': {
                    'title': "Error 'n_pages'",
                    'message': "Si ha escrito un libro tendrá que tener un mínimo de páginas ¿no?",
                },
            }
        if self.n_pages < 50:
            for record in self:
                self.extension = 'Ensayo'
        if self.n_pages <100:
            for record in self:
                self.extension = 'Corto'
        if self.n_pages >= 101:
            for record in self:
                self.extension = 'Largo'

	



class Awards(models.Model):
	_name = 'awards.model'

	name = fields.char(string = "Premio")
	yearAward = fields.Date(string = "Año en que ganó el premio")
	authors_id = fields.Many2many('book.model' string=" libros ganadores:")

	







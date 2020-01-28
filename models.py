from odoo import models, fields, api, exceptions
#from datetime import timedelta

class Libro(models.Model):
    _name = 'libro.model'

    nombre = fields.Char(string="NombreLibro")
    descripcion = fields.Text(string="Sinopsis del libro")
    fecha_lanzamiento = fields.Date(string="Dia de publicación", store=True)
    genero = fields.Selection([('gr1', 'Fantasia'), ('gr2', 'Ciencia ficción'), ('gr3','Romance'), ('gr4','Aventura'), ('gr5','Misterio'), ('gr6', 'Distópica')], 'Género', default='gr1')
    id_premio = fields.Many2many('id_premio', string="Premios")
    

class Author(models.Model):
    _name = 'autor.model'

    nombre = fields.Char(string="Nombre")
    apellido = fields.Char(string="Apellido")
    fecha_nac = fields.Date(string="Fecha de nacimiento", store=True)
    edad = fields.Integer('age')
    id_premio = fields.One2many('id_premio', 'id_autor', string="Premios")

class Prize(models.Model):
    _name = 'premio.model'

    tipoPremio = fields.Selection([('p1', 'Literatura'), ('p2', 'Man Book International'), ('p3','Miguel Cervantes'), ('p4','Goncourt'), ('p5','Franz Kafka')], 'Premios', default='p1')
    id_autor = fields.Many2one('autor.model', ondelete='cascade', string="Autor", required=True)

    
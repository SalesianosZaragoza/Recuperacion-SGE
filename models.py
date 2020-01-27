from datetime import timedelta
from odoo import models, fields, api, exceptions
from odoo.exceptions import ValidationError

class autor(models.Model):
    _name = 'autor.modelo'
    _description = "Modulo Autor"
    _inherit = 'base.entidad'

    name = fields.Char(string="Nombre Autor", required=True)
    fnac = fields.Date(string="Fecha de nacimiento", store=True)
    libro_ids = fields.One2many('libro.modelo','autor_id', string="Libros del autor:")
    premioautor_ids = fields.One2many('premioautor.modelo','autor_id', string="Premios del autor:")
    anosprofesion = fields.Integer(string="Numero de anos siendo escritor")


    @api.multi
    def copy(self, default=None):
        default = dict(default or {})

        copied_count = self.search_count(
            [('name', '=like', u"Copia de {}%".format(self.name))])
        if not copied_count:
            new_name = u"Copia de {}".format(self.name)
        else:
            new_name = u"Copia de {} ({})".format(self.name, copied_count)

        default['name'] = new_name
        return super(autor, self).copy(default)

    _sql_constraints = [

        ('name_unique',
         'UNIQUE(name)',
         "Ya existe un autor con este nombre!"),
    ]

    

    @api.constrains('anosprofesion')
    def _check_something(self):
        for record in self:
            if record.anosprofesion > 40:
                   raise ValidationError("Demasiados años escribiendo: %s" % record.anosprofesion)
    # all records passed the test, don't return anything

class libro(models.Model):   
    _name = 'libro.modelo'
    _description = "Modulo Libro"
    _inherit = 'base.entidad'

    name = fields.Char(string="Nombre Libro", required=True)
    ano = fields.Date(string="Fecha de publicacion", store=True)
    autor_id = fields.Many2one('autor.modelo', string="Hecho por:")
    premiolibro_ids = fields.One2many('premiolibro.modelo','libro_id', string="Premios del libro:")
    start_date = fields.Date(string="Fecha tiendas", default=fields.Date.today)
    color = fields.Integer()

    @api.multi
    def copy(self, default=None):
        default = dict(default or {})

        copied_count = self.search_count(
            [('name', '=like', u"{}% Segunda parte".format(self.name))])
        if not copied_count:
            new_name = u"{} Segunda parte".format(self.name)
        else:
            new_name = u"{} ({}) Segunda parte".format(self.name, copied_count)

        default['name'] = new_name
        return super(libro, self).copy(default)

    _sql_constraints = [

        ('name_unique',
         'UNIQUE(name)',
         "Ya existe un libro con este nombre!"),
    ]

class premioAutor(models.Model):
    _name = 'premioautor.modelo'
    _description = "Modulo premio"
    _inherit = 'base.entidad'

    name = fields.Char(string="Nombre premio", required=True)
    ano = fields.Date(string="Fecha de entrega", store=True)
    autor_id = fields.Many2one('autor.modelo', string="Autores que tienen este premio:")
    

class premioLibro(models.Model):
    _name = 'premiolibro.modelo'
    _description = "Modulo premio"
    _inherit = 'base.entidad'

    name = fields.Char(string="Nombre premio", required=True)
    ano = fields.Date(string="Fecha de entrega", store=True)
    libro_id = fields.Many2one('libro.modelo', string="Libros que tienen este premio:")
   
from datetime import timedelta
from odoo import models, fields, api, exceptions

class Autor(models.Model):
    _name = 'autor.modelo'
    _description = "Modulo Autor"
    _inherit = 'base.entidad'

    name = fields.Char(string="Nombre", required=True)
    libro_id = fields.One2many('libro.modelo', 'autor_id', string="libro")
    premio_id = fields.Many2many(
        'premio.modelo', 'autor_premio', 'autor_id', 'premio_id', 'premio')
    festival_id =fields.Many2one('festival.modelo',string='festival')
    premioPuesto=fields.Selection(selection=[('1', 'Primer premio'), ('2', 'Segundo premio'), (
        '3', 'Tercer premio')], string="Premio", default="1")
    age = fields.Char(string="Edad" , required=True)

    @api.constrains('age')
    def _check_something(self):
        for record in self:
            if record.age > 65:
                raise ValidationError("Un autor no puede ser mayor de 65 años: %s" % record.age)

class Libro(models.Model):
    _name = 'libro.modelo'
    _description = "Modulo Libro"
    _inherit = 'base.entidad'

    name = fields.Char(string="Nombre", required=True)
    autor_id =fields.Many2one('autor.modelo',string='autor')
    tapaDura = fields.Selection(selection=[('1','Si'), ('2','No')], string="Es de tapa dura",default="1")
    tiempo = fields.Selection(selection=[('1', '1 Hora'), ('2', '3 Horas'), (
        '3', '6 o mas Horas'), ('4','Un porron de horas')], string="categoria del libro", default="1", compute="_libro_tiempo")
    tamaño = fields.Char(string="tamaño", compute="_calcular_tamaño")
    paginaslibro = fields.Integer(string="paginaslibro") 
    start_date = fields.Date(string="Fecha tiendas", default=fields.Date.today)
    color = fields.Integer()
     
    @api.one
    def _calcular_tamaño(self):

            if paginaslibro < 100:
                self.tamaño = "corto"
            if paginaslibro > 100 and paginaslibro <=300:
                self.tamaño = "medio"
            if paginaslibro > 300 and paginaslibro <= 1000:
                self.tamaño = "largo"
            if paginaslibro > 1000:
                self.tamaño = "larguisimo"

    @api.one
    def _libro_tiempo(self):

            if self.tamaño == "corto":
                self.tiempo = '1'
            if self.tamaño == "medio":
                self.tiempo = '2'
            if self.tamaño == "largo":
                self.tiempo = '3'
            if self.tamaño == "larguisimo":
                self.tiempo = "4"

class Premio(models.Model):
    _name = 'premio.modelo'
    _description = "Modulo Premio"
    _inherit = 'base.entidad'

    name = fields.Char(string="Nombre", required=True)
    year = fields.Char(string="Fecha de publicacion", required=True)
    autor_id = fields.Many2many(
        'autor.modelo', 'autor_premio', 'premio_id', 'autor_id', 'autor')

class Festival(models.Model):
    _name = 'festival.modelo'
    _description = "Modulo Festival"
    _inherit = 'base.entidad'

    name = fields.Char(string="Nombre", required=True)
    date = fields.Date(string="Fecha del Festival", store=True)
    autor_id = fields.One2many('autor.modelo', 'festival_id', string="autor")
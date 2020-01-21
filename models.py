# -*- coding: utf-8 -*-
from odoo import models, fields, api


class autor(models.Model):
    _name = 'views.autor'
    name = fields.Char(string="Nombre Autor", required=True)
    fnac = fields.Date(string="fecha de nacimiento", store=True)
    libro_id = fields.One2many('views.libro', 'autor_id', string="libro")
    premio_id = fields.Many2many(
        'views.premio', 'autor_premio', 'autor_id', 'premio_id', 'premio')
    festival_id =fields.Many2one('views.festival',string='festival')
    premioPuesto= fields.Selection(selection=[('1', 'Primer premio'), ('2', 'Segundo premio'), (
    '3', 'Tercer premio')], string="Premio", default="1")
    

class libro(models.Model):
    _name = 'views.libro'
    title = fields.Char(string="Titulo Libro", required=True)
    autor_id =fields.Many2one('views.autor',string='autor')
    tapaDura = fields.Selection(selection=[('1','Si'), ('2','No')], string="Es de tapa dura",default="1")
    tiempo = fields.Selection(selection=[('1', '1 Hora'), ('2', '3 Horas'), (
        '3', '6 o mas Horas'), ('4','Un porron de horas')], string="categoria del libro", default="1", compute="_libro_tiempo")
    tamaño = fields.Char(string="tamaño", compute="_calcular_tamaño")
    paginaslibro = fields.Integer(string="paginaslibro") 

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

class premio(models.Model):
    _name = 'views.premio'
    year = fields.Char(string="Fecha de publicacion", required=True)
    autor_id = fields.Many2many(
        'views.autor', 'autor_premio', 'premio_id', 'autor_id', 'autor')


class festival(models.Model):
    _name = 'views.festival'
    date = fields.Date(string="Fecha del Festival", store=True)
    autor_id = fields.One2many('views.autor', 'festival_id', string="autor")

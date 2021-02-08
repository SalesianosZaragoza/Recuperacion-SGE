from odoo import models, fields, 

class Species(models.Model):
    _name='NaturalParks.Species'



    Name = fields.Char(string="name of the species")
    Vulgar_Name = fields.Char(string="vulgar name of the species")
    AreaID = fields.Many2many('NaturalParks.Area')
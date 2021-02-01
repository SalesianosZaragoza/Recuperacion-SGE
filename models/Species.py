from odoo import models, fields, 

class Species(models.Model):
    _name='NaturalParks.Species'



    Name = fields.Char()
    Vulgar_Name = fields.Char()
    AreaID = fields.Many2many('NaturalParks.Area')
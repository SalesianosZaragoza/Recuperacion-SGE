from odoo import models, fields, api

class Species(models.Model):
    _name='NaturalParks.Species'
    _order='Name'



    Name = fields.Char(string="name of the species")
    VulgarName = fields.Char(string="vulgar name of the species")
    NumberOfSpecimens = fields.Integer()


    AreaID = fields.Many2many('NaturalParks.Area')


    @api.constrains('NumberOfSpecimens')
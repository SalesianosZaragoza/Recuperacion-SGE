from odoo import models, fields, 

class Visitor(models.Model):
    _name='NaturalParks.Visitor'



    Name = fields.Char()
    DNI = fields.Char()
    Address = fields.Char()
    Job = fields.Char()


    LodgingID = fields.Many2one('NaturalParks.Lodging')
    NaturalParkID = fields.Many2one('NaturalParks.NaturalPark')
from odoo import models, fields, 

class Area(models.Model):
    _name='NaturalParks.Area'



    Name = fields.Char()
    Extension = fields.Integer()
    
    NaturalParkID = fields.Many2one('NaturalParks.NaturalPark')
    CommunityID = fields.Many2one('NaturalParks.Community')

    
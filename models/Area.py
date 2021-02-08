from odoo import models, fields, 

class Area(models.Model):
    _name='NaturalParks.Area'



    Name = fields.Char(string="name of the area")
    Extension = fields.Integer(string="kilometres of the area")
    
    NaturalParkID = fields.Many2one('NaturalParks.NaturalPark')
    CommunityID = fields.Many2one('NaturalParks.Community')

    
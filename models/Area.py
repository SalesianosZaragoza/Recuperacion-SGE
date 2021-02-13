from odoo import models, fields, api

class Area(models.Model):
    _name='NaturalParks.Area'
    _order='Name'



    Name = fields.Char(string="name of the area")
    Extension = fields.Integer(string="kilometres")
    
    NaturalParkID = fields.Many2one('NaturalParks.NaturalPark')
    CommunityID = fields.Many2one('NaturalParks.Community')

    @api.constrains('Extension')

    @api.constrains('NaturalParkID', 'CommunityID')

    
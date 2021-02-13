from odoo import models, fields, api

class NaturalPark(models.Model):
    _name='NaturalParks.NaturalPark'
    _order='Name'



    Name = fields.Char(string="name of the natural park")
    StatementDate = fields.Date()
    

    CommunityID = fields.Many2many('NaturalParks.Community')

    @api.constrains('Extension')
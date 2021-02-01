from odoo import models, fields, 

class NaturalPark(models.Model):
    _name='NaturalParks.NaturalPark'



    Name = fields.Char()
    Statement_Date = fields.Date()
    Extension = fields.Integer()

    CommunityID = fields.Many2many('NaturalParks.Community')
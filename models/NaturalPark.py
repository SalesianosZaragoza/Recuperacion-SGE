from odoo import models, fields, 

class NaturalPark(models.Model):
    _name='NaturalParks.NaturalPark'



    Name = fields.Char(string="name of the natural park")
    Statement_Date = fields.Date()
    

    CommunityID = fields.Many2many('NaturalParks.Community')
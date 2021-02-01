from odoo import models, fields, 

class Lodging(models.Model):
    _name='NaturalParks.Lodging'



    Name = fields.Char()
    Capacity = fields.Intereger()
    


    NaturalParkID = fields.Many2one('NaturalParks.NaturalPark')

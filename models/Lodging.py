from odoo import models, fields, 

class Lodging(models.Model):
    _name='NaturalParks.Lodging'



    Name = fields.Char(string="name of the lodging")
    Capacity = fields.Intereger(string="capacity of the lodging")
    Category = fields.Selection([('first class'),('second class'), ('third class')])
    


    NaturalParkID = fields.Many2one('NaturalParks.NaturalPark')

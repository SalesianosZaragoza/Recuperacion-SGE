from odoo import models, fields, api, exceptions

class NaturalPark(models.Model):
    _name='NaturalParks.NaturalPark'



    Name = fields.Char(string="Name", required=True)
    Statement_Date = fields.Date()
    Extension =
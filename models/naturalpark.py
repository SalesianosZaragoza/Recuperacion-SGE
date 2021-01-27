from odoo import models

class NaturalPark(models.Model):
    _name = 'appnaturalparks.naturalpark'

    name = fields.Char(string="Name", required=True)
    starting_date = fields.Date()
    extension = fields.Integer(string="Extension (in km2)", required=True)
    

    
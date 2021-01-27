from odoo import models

class Area(models.Model):
    _name = 'appnaturalparks.area'

    name = fields.Char(string="Name", required=True)
    extension = fields.Integer(string="Extension (in km2)", required=True)
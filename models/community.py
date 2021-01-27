from odoo import models

class Community(models.Model):
    _name = 'appnaturalparks.community'
    
    name = fields.Char(string="Name", required=True)
    administrative_authority = fields.Char(required=True)
    extension = fields.Integer(string="Extension (in km2)", required=True)

    
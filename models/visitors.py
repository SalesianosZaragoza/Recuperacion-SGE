from odoo import models

class Visitors(models.Model):
    _name = 'appnaturalparks.visitors'

    name = fields.Char(required=True)    
    dni = fields.Char(required=True)
    address = fields.Char()
    job = fields.Char()
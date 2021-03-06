from odoo import models, fields

class Community(models.Model):
    _name = 'RecuperacionOdooCristianMarin.community'

    name = fields.Char(string="name")
    extension = fields.Integer(string="extension")
    responsible_body = fields.Char() 


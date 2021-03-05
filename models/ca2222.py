from odoo import models, fields, api

class ca(models.Model):
    _name = 'npi.ca'

    name = fields.Char(string="Nombre")
    extension = fields.Integer(string="Extension")
    responsible_body = fields.Char() 
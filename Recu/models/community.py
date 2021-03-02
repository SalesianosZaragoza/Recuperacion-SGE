from odoo import models, fields, api, exceptions

class Community(models.Model):
    _name = 'recu.community'

    name = fields.Char(string="Nombre")
    extension = fields.Integer(string="Extension")
    responsible_body = fields.Char() 


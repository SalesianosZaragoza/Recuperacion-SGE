from odoo import models, fields

class Community(models.Model):
    _name = 'naturalparks.community'
    _order = 'name'

    name = fields.Char(string="Name", required=True)
    length = fields.Integer(string="length", required=True)
    administrative_authority = fields.Char(required=True)

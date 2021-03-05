from odoo import models, fields, api

class naturalPark(models.Model):
    _name = 'npi.naturalPark'

    name = fields.Char(string="Name", required=True)
    starting_date = fields.Date()
    extension = fields.Integer(string="Extension", required=True)
from odoo import models, fields, api

class NaturalPark(models.Model):
    _name = 'npi.NaturalPark'

    name = fields.Char(string="Name", required=True)
    starting_date = fields.Date()
    extension = fields.Integer(string="Extension", required=True)
from odoo import models, fields, api

class Hostel(models.Model):
    _name = 'npi.Hostel'

    name = fields.Char(string="Name", required=True)
    occupation = fields.Integer(string="Occupation", required=True)
    capacity = fields.Integer(string="Capacity", required=True)


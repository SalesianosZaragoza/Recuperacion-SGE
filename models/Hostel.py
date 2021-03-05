from odoo import models, fields, api

class hostel(models.Model):
    _name = 'npi.hostel'

    name = fields.Char(string="Name", required=True)
    occupation = fields.Integer(string="Occupation", required=True)
    capacity = fields.Integer(string="Capacity", required=True)


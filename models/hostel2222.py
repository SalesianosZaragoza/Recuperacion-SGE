from odoo import models, fields, api

class hostel(models.Model):
    _name = 'npi.hostel'

    name = fields.Char(string="Name", required=True)
    occupation = fields.Integer(string="Occupation")
    capacity = fields.Integer(string="Capacity")

    naturalPark_id = fields.Many2one('npi.naturalPark', string="Natural Park")


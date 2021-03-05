from odoo import models, fields, api

class area(models.Model):
    _name = 'npi.area'

    name = fields.Char(string="Name", required=True)
    extension = fields.Integer(string="Extension", required=True)

    naturalPark_id = fields.Many2one('npi.naturalPark', string="Natural Park", required=True)
    ca_id = fields.Many2one('npi.ca', string="Autonomous community", required=True)
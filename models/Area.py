from odoo import models, fields, api

class Area(models.Model):
    _name = 'npi.Area'

    name = fields.Char(string="Name", required=True)
    extension = fields.Integer(string="Extension", required=True)

    NaturalPark_id = fields.Many2one('npi.NaturalPark', string="Natural Park", required=True)
    CA_id = fields.Many2one('npi.CA', string="Autonomous community", required=True)
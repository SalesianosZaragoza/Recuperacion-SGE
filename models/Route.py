from odoo import models, fields, api

class Route(models.Model):
    _name = 'npi.Route'

    name = fields.Char(string="Name of the route", required=True)
    way = fields.Selection([('vehicle', 'Vehicle'), ('walking', 'Walking')], required=True)
    numberOfPeople = fields.Integer(string="Number of people")


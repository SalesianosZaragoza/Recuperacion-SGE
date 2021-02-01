from odoo import models, fields, api

class Route(models.Model):
    _name = 'npi.Route'

    name = fields.Char(string="Name of the route", required=True)
    way = fields.Selection([('vehicle', 'Vehicle'), ('walking', 'Walking')], required=True)
    numberOfPeople = fields.Integer(string="Number of people")
    date = fields.Datetime(required=True)

    NaturalPark_id = fields.Many2one('npi.NaturalPark', string="Natural Park", required=True)
    Hostel_id = fields.Many2one('npi.Hostel', string="Hostel", required=True)
    Visitor_id = fields.Many2many('npi.Visitor', string="Visitor/s", required=True)

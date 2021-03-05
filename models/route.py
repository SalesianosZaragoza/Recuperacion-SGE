from odoo import models, fields, api

class route(models.Model):
    _name = 'npi.route'

    name = fields.Char(string="Name of the route", required=True)
    way = fields.Selection([('vehicle', 'Vehicle'), ('walking', 'Walking')])
    numberOfPeople = fields.Integer(string="Number of people")
    dateStart = fields.Datetime(string="Begin")
    dateStop = fields.Datetime(string="End")

    naturalPark_id = fields.Many2one('npi.naturalPark', string="Natural Park", required=True)
    hostel_id = fields.Many2one('npi.hostel', string="Hostel", required=True)
    visitor_id = fields.Many2many('npi.visitor', string="Visitor/s", required=True)

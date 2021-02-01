from odoo import models, fields, api

class Visitor(models.Model):
    _name = 'npi.Visitor'

    dni = fields.Char(string="D.N.I.", required=True)
    name = fields.Char(string="Name", required=True)
    adress = fields.Char(string="Dirección", required=True)
    job = fields.Char(string="Trabajo", required=True)
    
    NaturalPark_id = fields.Many2one('npi.NaturalPark', string="Natural Park", required=True)
    Managment_id = fields.Many2one('npi.Managment', string="Managment", required=True)
    Hostel_id = fields.Many2one('npi.Hostel', string="Hostel", required=True)
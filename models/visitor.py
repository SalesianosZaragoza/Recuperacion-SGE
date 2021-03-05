from odoo import models, fields, api

class visitor(models.Model):
    _name = 'npi.visitor'

    dni = fields.Char(string="D.N.I.", required=True)
    name = fields.Char(string="Name")
    adress = fields.Char(string="Dirección")
    job = fields.Char(string="Trabajo")
    
    naturalPark_id = fields.Many2one('npi.naturalPark', string="Natural Park", required=True)
    managment_id = fields.Many2one('npi.managment', string="Managment", required=True)
    hostel_id = fields.Many2one('npi.hostel', string="Hostel", required=True)
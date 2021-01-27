from odoo import models, fields, api

class Visitor(models.Model):
    _name = 'npi.Visitor'

    dni = fields.Char(string="D.N.I.", required=True)
    name = fields.Char(string="Name", required=True)
    adress = fields.Char(string="Dirección", required=True)
    job = fields.Char(string="Trabajo", required=True)
    
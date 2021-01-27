from odoo import models, fields, api

class Staff(models.Model):
    _name = 'npi.Staff'

    dni = fields.Char(string="D.N.I.", required=True)
    ss = fields.Char(string="Seguridad social", required=True)
    name = fields.Char(string="Name", required=True)
    adress = fields.Char(string="Dirección", required=True)
    mobile_phone = fields.Char(string="Teléfono móvil", required=True)
    landline = fields.Char(string="Teléfono fijo", required=True)
    salary = fields.Integer(string="Salario", required=True)
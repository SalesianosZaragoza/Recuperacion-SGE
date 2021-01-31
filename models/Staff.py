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


class Managment(models.Model):
    _name = 'npi.Managment'
    _inherit = 'npi.Staff'

    entry = fields.Selection([(('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'))])

class Vigilancy(models.Model):
    _name = 'npi.Vigilancy'
    _inherit = 'npi.Staff'


class Investigator(models.Model):
    _name = 'npi.Investigator'
    _inherit = 'npi.Staff'

    title = fields.Char(required = True)

class Conservation(models.Model):
    _name = 'npi.Conservation'
    _inherit = 'npi.Staff'

    specialization = fields.Selection([(('canine', 'Canine'), ('cleanning', 'Cleanning'), ('other', 'Other'))])
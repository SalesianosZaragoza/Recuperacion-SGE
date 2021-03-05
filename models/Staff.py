from odoo import models, fields, api

class staff(models.Model):
    _name = 'npi.Staff'

    dni = fields.Char(string="D.N.I.", required=True)
    ss = fields.Char(string="Seguridad social", required=True)
    name = fields.Char(string="Name", required=True)
    adress = fields.Char(string="Dirección", required=True)
    mobile_phone = fields.Char(string="Teléfono móvil", required=True)
    landline = fields.Char(string="Teléfono fijo", required=True)
    salary = fields.Integer(string="Salario", required=True)

    naturalPark_id = fields.Many2one('npi.naturalPark', string="Natural Park", required=True)


class managment(models.Model):
    _name = 'npi.managment'
    _inherit = 'npi.staff'

    entry = fields.Selection([(('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'))])

class vigilancy(models.Model):
    _name = 'npi.vigilancy'
    _inherit = 'npi.staff'

    area_id = fields.Many2one('npi.area', string="Area", required=True)


class investigator(models.Model):
    _name = 'npi.investigator'
    _inherit = 'npi.staff'

    title = fields.Char(required = True)

class conservation(models.Model):
    _name = 'npi.conservation'
    _inherit = 'npi.staff'

    specialization = fields.Selection([(('canine', 'Canine'), ('cleanning', 'Cleanning'), ('other', 'Other'))])

    area_id = fields.Many2one('npi.area', string="Area", required=True)
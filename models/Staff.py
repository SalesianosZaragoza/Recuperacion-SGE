from odoo import models, fields, api

class staff(models.Model):
    _name = 'npi.Staff'

    dni = fields.Char(string="D.N.I.", required=True)
    ss = fields.Char(string="Seguridad social")
    name = fields.Char(string="Name")
    adress = fields.Char(string="Dirección")
    mobile_phone = fields.Char(string="Teléfono móvil")
    landline = fields.Char(string="Teléfono fijo")
    salary = fields.Integer(string="Salario")

    naturalPark_id = fields.Many2one('npi.naturalPark', string="Natural Park", required=True)


class managment(models.Model):
    _name = 'npi.managment'
    _inherit = 'npi.staff'

    entry = fields.Selection([(('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'))])

class vigilancy(models.Model):
    _name = 'npi.vigilancy'
    _inherit = 'npi.staff'

    area_id = fields.Many2one('npi.area', string="Area")
    car_id = fields.Many2one('npi.car', string="Car")

class investigator(models.Model):
    _name = 'npi.investigator'
    _inherit = 'npi.staff'

    title = fields.Char(required = True)

class conservation(models.Model):
    _name = 'npi.conservation'
    _inherit = 'npi.staff'

    specialization = fields.Selection([(('canine', 'Canine'), ('cleanning', 'Cleanning'), ('other', 'Other'))])

    area_id = fields.Many2one('npi.area', string="Area", required=True)

class car(models.Model):
    _name = 'npi.car'

    model = fields.Char(string="Type of car", required=True)
    enrollment = fields.Char(string="Enrollment")


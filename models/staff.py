from odoo import models, fields

class Staff(models.Model):
    _name = 'recu.staff'

    dni = fields.Char(string="Dni")
    social_security = fields.Char(string="Seguridad Social")  
    name = fields.Char(string="Nombre")
    address = fields.Char(string="Direccion")
    landline = fields.Integer()
    mobile_phone = fields.Integer()
    salary = fields.Integer(string="Salario") 
    natural_park_id = fields.Many2one('recu.natural_park', ondelete='cascade', string="Parque Natural")

class Management(models.Model):
    _name = 'recu.management'
    _inherit = 'recu.staff'

    number_entrance = fields.Integer(string="Numero de entrada")

class Vigilance(models.Model):
    _name = 'recu.vigilance'
    _inherit = 'recu.staff'

    car_id = fields.Many2one('recu.car', string="Car")
    area_id = fields.Many2one('recu.area', string="Area")

class Research(models.Model):
    _name = 'recu.research'
    _inherit = 'recu.staff'

    title = fields.Char()

class Conservation(models.Model):
    _name = 'recu.conservation'
    _inherit = 'recu.staff'

    area_id = fields.Many2one('recu.area', string="Area")
    specialty = fields.Selection([('cleaning', 'Limpieza'), ('roads', 'Caminos')]) 

class Car(models.Model):
    _name = 'recu.car'

    type = fields.Char(string="Tipo")
    enrollment = fields.Char(string="Matricula")

class Project(models.Model):
    _name = 'recu.project'

    name = fields.Char(string="Nombre")
    budget = fields.Float(string="Fondos")
    project_time = fields.Integer(string="Tiempo de realizacion")
    species_id = fields.Many2one('recu.species', string="Especies")
    research_ids = fields.Many2many('recu.research', string="Investigadores")


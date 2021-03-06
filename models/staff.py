from odoo import models, fields

class Staff(models.Model):
    _name = 'odoonp.staff'

    dni = fields.Char(string="Dni")
    social_security = fields.Char(string="Seguridad Social")  
    name = fields.Char(string="Nombre")
    address = fields.Char(string="Direccion")
    landline = fields.Integer()
    mobile_phone = fields.Integer()
    salary = fields.Integer(string="Salario") 
    natural_park_id = fields.Many2one('odoonp.natural_park', ondelete='cascade', string="Natural Park")

class Management(models.Model):
    _name = 'odoonp.management'
    _inherit = 'odoonp.staff'

    number_entrance = fields.Integer(string="Entrance number")

class Vigilance(models.Model):
    _name = 'odoonp.vigilance'
    _inherit = 'odoonp.staff'

    car_id = fields.Many2one('odoonp.car', string="Car")
    area_id = fields.Many2one('odoonp.area', string="Area")

class Research(models.Model):
    _name = 'odoonp.research'
    _inherit = 'odoonp.staff'

    title = fields.Char()

class Conservation(models.Model):
    _name = 'odoonp.conservation'
    _inherit = 'odoonp.staff'

    area_id = fields.Many2one('odoonp.area', string="Area")
    specialty = fields.Selection([('cleaning', 'Limpieza'), ('roads', 'Caminos')]) 

class Car(models.Model):
    _name = 'odoonp.car'

    type = fields.Char(string="Tipo")
    enrollment = fields.Char(string="Matricula")

class Project(models.Model):
    _name = 'odoonp.project'

    name = fields.Char(string="Nombre")
    budget = fields.Float(string="Fondos")
    project_time = fields.Integer(string="Tiempo de realizacion")
    species_id = fields.Many2one('odoonp.species', string="Especies")
    research_ids = fields.Many2many('odoonp.research', string="Investigadores")
from odoo import models, fields

class Management(models.Model):
    _name = 'naturalP.management'
    _order = 'name'
    _inherit = 'naturalP.staff'

    tickets = fields.Integer()

class Research(models.Model):
    _name = 'naturalP.research'
    _order = 'name'
    _inherit = 'naturalP.staff'

    title = fields.Char(required=True)

class Surveillance(models.Model):
    _name = 'naturalP.surveillance'
    _order = 'name'
    _inherit = 'naturalP.staff'

    area_id = fields.Many2one('naturalP.area', string="Area", required=True)
    car_id = fields.Many2one('naturalP.car', string="Car", required=True)

class Conservation(models.Model):
    _name = 'naturalP.conservation'
    _order = 'name'
    _inherit = 'naturalP.staff'

    area_id = fields.Many2one('naturalP.area', string="Area", required=True)
    special_field = fields.Selection([('cleaning', 'Cleaning'), ('roads', 'Roads')]) 

class Car(models.Model):
    _name = 'naturalP.car'
    _order = 'name'

    name = fields.Char(string="Car Type", required=True)
    car_registration = fields.Char(string="Registration")

class Staff(models.Model):
    _name = 'naturalP.staff'

    name = fields.Char(string="Name", required=True)
    dni = fields.Char(required=True)
    security = fields.Char(required=True)
    natural_park_id = fields.Many2one('naturalP.natural_park', ondelete='cascade', string="Natural Park", required=True)
    address = fields.Char()
    phone = fields.Char()
    telephone = fields.Char()
    salary = fields.Integer(string="Salary")
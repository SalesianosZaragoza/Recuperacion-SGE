from odoo import models, fields

class Management(models.Model):
    _name = 'naturalparks.management'
    _order = 'name'
    _inherit = 'naturalparks.staff'

    tickets = fields.Integer()

class Research(models.Model):
    _name = 'naturalparks.research'
    _order = 'name'
    _inherit = 'naturalparks.staff'

    title = fields.Char(required=True)

class Surveillance(models.Model):
    _name = 'naturalparks.surveillance'
    _order = 'name'
    _inherit = 'naturalparks.staff'

    area_id = fields.Many2one('naturalparks.area', string="Area", required=True)
    car_id = fields.Many2one('naturalparks.car', string="Car", required=True)

class Conservation(models.Model):
    _name = 'naturalparks.conservation'
    _order = 'name'
    _inherit = 'naturalparks.staff'

    area_id = fields.Many2one('naturalparks.area', string="Area", required=True)
    special_field = fields.Selection([('cleaning', 'Cleaning'), ('roads', 'Roads'), ('others', 'Others')]) 

class Car(models.Model):
    _name = 'naturalparks.car'
    _order = 'name'

    name = fields.Char(string="Car Type", required=True)
    number_plate = fields.Char(string="Number Plate")
    color = fields.Integer()
    image = fields.Binary(string="Car Image", max_width=100, max_height=100, verify_resolution=False)

class Staff(models.Model):
    _name = 'naturalparks.staff'

    name = fields.Char(string="Name", required=True)
    dni = fields.Char(required=True)
    security = fields.Char(required=True)
    natural_park_id = fields.Many2one('naturalparks.natural_park', ondelete='cascade', string="Natural Park", required=True)
    address = fields.Char()
    phone = fields.Char()
    telephone = fields.Char()
    salary = fields.Integer(string="Salary")
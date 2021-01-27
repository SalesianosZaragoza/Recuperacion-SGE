from odoo import models

class Staff(models.Model):
    _name = 'appnaturalparks.staff'

    name = fields.Char(string="Name", required=True)
    dni = fields.Char(required=True)
    social_security = fields.Char(required=True)
    address = fields.Char()
    mobile_phone = fields.Char()
    landline = fields.Char()
    salary = fields.Integer(string="Salary (in €, annual)")
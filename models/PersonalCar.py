from odoo import models, fields

class PersonalCar(models.Model):
    _name = 'NaturalParks.PersonalCar'
    _order = 'name'
    

    name = fields.Char(string="PersonalCar Model")
    Enrollment = fields.Char()
    
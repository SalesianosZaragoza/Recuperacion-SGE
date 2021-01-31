from odoo import models, fields, api, exceptions

class ParkPersonal(models.Model):
    _name='NaturalParks.ParkPersonal'


    Name = fields.Char(string="Name", required=True)
    DNI = fields.Char(required=True)
    SS_Number = fields.Char(required=True)
    Address = fields.char()
    Mobile_Phone = fields.Char()
    Home_Phone = fields.Char()
    Salary = 
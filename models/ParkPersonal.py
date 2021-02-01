from odoo import models, fields, 

class ParkPersonal(models.Model):
    _name='NaturalParks.ParkPersonal'


    Name = fields.Char()
    DNI = fields.Char()
    SS_Number = fields.Char()
    Address = fields.char()
    Mobile_Phone = fields.Char()
    Home_Phone = fields.Char()
    Salary = fields.Integer() 


    NaturalParkID = fields.Many2one('NaturalParks.NaturalPark')
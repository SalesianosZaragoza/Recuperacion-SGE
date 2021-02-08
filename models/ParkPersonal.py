from odoo import models, fields, 

class ParkPersonal(models.Model):
    _name='NaturalParks.ParkPersonal'


    Name = fields.Char(string="name of the employee")
    DNI = fields.Char(string="DNI of the employee")
    SS_Number = fields.Char(string="social security number of the employee")
    Address = fields.char(string="address of the employee")
    Mobile_Phone = fields.Char(string="mobile phone number of the employee")
    Home_Phone = fields.Char(string="home phone number of the employee")
    Salary = fields.Integer(string="salary of the employee") 


    NaturalParkID = fields.Many2one('NaturalParks.NaturalPark')
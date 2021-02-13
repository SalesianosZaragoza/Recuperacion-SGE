from odoo import models, fields, api

class ParkPersonal(models.Model):
    _name='NaturalParks.ParkPersonal'
    _order='Name'


    Name = fields.Char(string="name of the employee")
    DNI = fields.Char(string="DNI of the employee")
    SSNumber = fields.Char(string="social security number of the employee")
    Address = fields.char(string="address of the employee")
    MobilePhone = fields.Char(string="mobile phone number of the employee")
    HomePhone = fields.Char(string="home phone number of the employee")
    Salary = fields.Integer(string="salary of the employee") 


    NaturalParkID = fields.Many2one('NaturalParks.NaturalPark')

    @api.constrains('Salary')
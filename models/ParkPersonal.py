from odoo import models, fields, api, exceptions

class ParkPersonal(models.Model):
    _name='NaturalParks.ParkPersonal'
    _order='name'


    name = fields.Char(string="name of the employee")
    DNI = fields.Char(string="DNI of the employee")
    SSNumber = fields.Char(string="social security number of the employee")
    Address = fields.Char(string="address of the employee")
    MobilePhone = fields.Char(string="mobile phone number of the employee")
    HomePhone = fields.Char(string="home phone number of the employee")
    Salary = fields.Integer(string="salary of the employee") 


    NaturalParkID = fields.Many2one('NaturalParks.NaturalPark')

    @api.constrains('Salary')
    def _How_Much_Salary_Has_The_Employee(self):
        for r in self:
            if r.salary <= 0:
                raise exceptions.ValidationError("error")
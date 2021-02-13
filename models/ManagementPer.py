from odoo import models, fields, 

class ManagementPer(models.Model):
    _name='NaturalParks.ManagementPer'
    _order='Name'
    _inherit='NaturalParks.ParkPersonal'


    Name = fields.Char(string="name of the employee")
    NumberOfEntry = fields.integer()
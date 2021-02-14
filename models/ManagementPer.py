from odoo import models, fields

class ManagementPer(models.Model):
    _name='NaturalParks.ManagementPer'
    _order='name'
    _inherit='NaturalParks.ParkPersonal'


    name = fields.Char(string="name of the employee")
    NumberOfEntry = fields.Integer()
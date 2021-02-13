from odoo import models, fields, 

class ResearchPer(models.Model):
    _name='NaturalParks.ResearchPer'
    _order='Name'
    _inherit='NaturalParks.ParkPersonal'


    Name = fields.Char(string="name of the employee")
    Title = fields.char(string="title of the employee")
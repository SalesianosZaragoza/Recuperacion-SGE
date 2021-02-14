from odoo import models, fields 

class ResearchPer(models.Model):
    _name='NaturalParks.ResearchPer'
    _order='name'
    _inherit='NaturalParks.ParkPersonal'


    name = fields.Char(string="name of the employee")
    Title = fields.Char(string="title of the employee")
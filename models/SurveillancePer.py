from odoo import models, fields, 

class SurveillancePer(models.Model):
    _name='NaturalParks.SurveillancePer'
    _order='Name'
    _inherit='NaturalParks.ParkPersonal'


    Name = fields.Char(string="name of the employee")
    

    AreaID = fields.Many2one('NaturalParks.Area')
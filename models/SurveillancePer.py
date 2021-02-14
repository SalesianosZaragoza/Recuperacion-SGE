from odoo import models, fields 

class SurveillancePer(models.Model):
    _name='NaturalParks.SurveillancePer'
    _order='name'
    _inherit='NaturalParks.ParkPersonal'


    name = fields.Char(string="name of the employee")
    

    AreaID = fields.Many2one('NaturalParks.Area')
    Enrollment = fields.Many2one('NaturalParks.PersonalCar')
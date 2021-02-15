from odoo import models, fields, api, exceptions 
from odoo.exceptions import ValidationError
class SurveillancePer(models.Model):
    _name='NaturalParks.SurveillancePer'
    _inherit='NaturalParks.ParkPersonal'


    
    

    AreaID = fields.Many2one('NaturalParks.Area')
    Enrollment = fields.Many2one('NaturalParks.PersonalCar')

class PersonalCar(models.Model):
    _name = 'NaturalParks.PersonalCar'
    _order = 'name'
    

    name = fields.Char(string="PersonalCar Model")
    Enrollment = fields.Char()
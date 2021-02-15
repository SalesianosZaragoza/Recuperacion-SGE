from odoo import models, fields 
from odoo.exceptions import ValidationError
class ResearchPer(models.Model):
    _name='NaturalParks.ResearchPer'
    _inherit='NaturalParks.ParkPersonal'


    
    Title = fields.Char(string="title of the employee")
from odoo import models, fields, api, exceptions 
from odoo.exceptions import ValidationError
class ConservationPer(models.Model):
    _name='NaturalParks.ConservationPer'
    
    _inherit='NaturalParks.ParkPersonal'


    
    Specialty = fields.Selection([('cleaning', 'Cleaning'), ('roads', 'Roads'), ('others', 'Others')])
    

    AreaID = fields.Many2one('NaturalParks.Area')


from odoo import models, fields, api, exceptions
from odoo.exceptions import ValidationError
class ManagementPer(models.Model):
    _name='NaturalParks.ManagementPer''
    _inherit='NaturalParks.ParkPersonal'


    
    NumberOfEntry = fields.Integer()
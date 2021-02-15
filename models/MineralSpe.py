from odoo import models, fields, api, exceptions 
from odoo.exceptions import ValidationError
class MineralSpe(models.Model):
    _inherit='NaturalParks.Species'
    _name='NaturalParks.MineralSpe'
    


    MineralType = fields.Selection([('crystal', 'Crystal'), ('stone', 'Stone')])
   
from odoo import models, fields, 

class MineralSpe(models.Model):
    _inherit='NaturalParks.Species'
    _name='NaturalParks.MineralSpe'
    _order='name'


    Mineral_Type = fields.Selection()
   
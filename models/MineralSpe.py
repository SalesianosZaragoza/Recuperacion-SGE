from odoo import models, fields 

class MineralSpe(models.Model):
    _inherit='NaturalParks.Species'
    _name='NaturalParks.MineralSpe'
    _order='name'


    MineralType = fields.Selection([('crystal', 'Crystal'), ('stone', 'Stone')])
   
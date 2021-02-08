from odoo import models, fields, 

class AnimalSpe(models.Model):
    _inherit='NaturalParks.Species'
    _name='NaturalParks.AnimalSpe'
    _order='name'


    Alimentation = fields.Selection()
    Heat_Season = fields.Selection()
    Depredated =
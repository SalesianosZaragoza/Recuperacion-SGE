from odoo import models, fields, api

class VegetableSpe(models.Model):
    _inherit='NaturalParks.Species'
    _name='NaturalParks.VegetableSpe'
    _order='Name'


    Flowering = fields.Boolean(String='flowering?Y/N?')
    FloweringSeason = fields.Selection([('summer', 'Summer'), ('autumn', 'Autumn'), ('winter', 'Winter'),('spring', 'Spring')])
    Depredated = fields.Boolean(String="is depredated?")

    AnimalID = fields.Many2many('NaturalParks.AnimalSpe')

    @api.constrains('Flowering','FloweringSeason')

    @api.constrains('Depredated','AnimalID')
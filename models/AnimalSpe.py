from odoo import models, fields, api

class AnimalSpe(models.Model):
    _inherit='NaturalParks.Species'
    _name='NaturalParks.AnimalSpe'
    _order='Name'


    Alimentation = fields.Selection([('carnivore','Carnivore'),('omnivore','Omnivore'),('herbivore','Herbivore')])
    HeatSeason = fields.Selection([('summer','Summer'),('autumm','Autumm'),('winter','Winter'),('spring','Spring')])
    Depredated = fields.Boolean(String="is depredated?")

    AnimalID = fields.Many2many('NaturalParks.AnimalSpe')

    @api.constrains('Depredated', 'AnimalID')
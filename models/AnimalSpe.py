from odoo import models, fields, api, exceptions

class AnimalSpe(models.Model):
    _inherit='NaturalParks.Species'
    _name='NaturalParks.AnimalSpe'
    _order='name'


    Alimentation = fields.Selection([('carnivore','Carnivore'),('omnivore','Omnivore'),('herbivore','Herbivore')])
    HeatSeason = fields.Selection([('summer','Summer'),('autumm','Autumm'),('winter','Winter'),('spring','Spring')])
    Depredated = fields.Boolean(String="is depredated?")

    AnimalIDS = fields.Many2many('NaturalParks.AnimalSpe')

    @api.constrains('Depredated', 'AnimalID')
    def _How_Is_The_Animals_Alimentation(self):
        for r in self:
            if not r.Depredated and r.AnimalID:
                raise exceptions.ValidationError("error")
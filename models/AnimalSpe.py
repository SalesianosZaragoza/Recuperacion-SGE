from odoo import models, fields, api, exceptions
from odoo.exceptions import ValidationError
class AnimalSpe(models.Model):
    _inherit='NaturalParks.Species'
    _name='NaturalParks.AnimalSpe'
    


    Alimentation = fields.Selection([('carnivore','Carnivore'),('omnivore','Omnivore'),('herbivore','Herbivore')])
    HeatSeason = fields.Selection([('summer','Summer'),('autumm','Autumm'),('winter','Winter'),('spring','Spring')])
    Depredated = fields.Boolean(String="is depredated")

    AnimalIDS = fields.Many2many(comodel_name='NaturalParks.AnimalSpe', relation='animals_eaten', column1='prey', column2='carnivores',
        domain=[('alimentation', '!=', 'herbivore')])

    @api.constrains('Depredated', 'AnimalIDS')
    def _How_Is_The_Animals_Alimentation(self):
        for r in self:
            if not r.Depredated and r.AnimalID:
                raise exceptions.ValidationError("error")
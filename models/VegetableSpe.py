from odoo import models, fields, api, exceptions
from odoo.exceptions import ValidationError
class VegetableSpe(models.Model):
    _inherit='NaturalParks.Species'
    _name='NaturalParks.VegetableSpe'
    


    Flowering = fields.Boolean(String='flowering?Y/N?')
    FloweringSeason = fields.Selection([('summer', 'Summer'), ('autumn', 'Autumn'), ('winter', 'Winter'),('spring', 'Spring')])
    Depredated = fields.Boolean(String="is depredated?")

    AnimalIDS = fields.Many2many('NaturalParks.AnimalSpe', 
        domain=[('alimentation', '!=', 'carnivore')])

    @api.constrains('Flowering','FloweringSeason')
    def _Has_The_Plant_Flowering(self):
        for r in self:
            if not r.Flowering and r.FloweringSeason:
                raise exceptions.ValidationError("error")

    @api.constrains('Depredated','AnimalIDS')
    def _How_Is_The_Animals_Alimentation(self):
        for r in self:
            if not r.Depredated and r.AnimalID:
                raise exceptions.ValidationError("error")
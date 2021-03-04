from odoo import models, fields, api, exceptions

class Species(models.Model):
    _name = 'naturalparks.species'

    name = fields.Char(string="scientific name", required=True)
    vulgar_name = fields.Char(string="vulgar name", required=True)
    area_ids = fields.Many2many('naturalparks.area', string="Area", required=True)
    number_of_specimens = fields.Integer()

    @api.constrains('number_of_specimens')
    def _check_number_is_positive(self):
        for r in self:
            if r.number_of_specimens <= 0:
                raise exceptions.ValidationError("error")

class Vegetablespe(models.Model):
    _name = 'naturalparks.vegetablespe'
    _inherit = 'naturalparks.species'
    _order = 'name'

    flowering = fields.Boolean(string="Does the vegetable have flowering?")
    flowering_season = fields.Selection([('spring', 'Spring'), ('summer', 'Summer'), ('autumn', 'Autumn'), ('winter', 'Winter')])

    depredated = fields.Boolean(string="Is this vegetable depredated?")
    animalspe_ids = fields.Many2many('naturalparks.animalspe', string="Herbivores which eat this vegetable", 
        domain=[('alimentation', '!=', 'carnivore')])

    @api.constrains('flowering', 'flowering_season')
    def _check_plant_has_flowering(self):
        for r in self:
            if not r.flowering and r.flowering_season:
                raise exceptions.ValidationError("error")

    @api.constrains('depredated', 'animalspe_ids')
    def _check_animals_are_herbivores_or_omnivores(self):
        for r in self:
            if not r.depredated and r.animalspe_ids:
                raise exceptions.ValidationError("error")


class Animalspe(models.Model):
    _name = 'naturalparks.animalspe'
    _inherit = 'naturalparks.species'
    _order = 'name'

    alimentation = fields.Selection([('carnivore','Carnivore'), ('herbivore','Herbivore'), ('omnivore','Omnivore')], required=True)
    heat_season = fields.Selection([('spring', 'Spring'), ('summer', 'Summer'), ('autumn', 'Autumn'), ('winter', 'Winter')])

    depredated = fields.Boolean(string="Is this animal depredated?")
    animalspe_ids = fields.Many2many(comodel_name='naturalparks.animalspe', relation='animals_eaten', column1='prey', column2='carnivores', string="Carnivores which eat this animal",
        domain=[('alimentation', '!=', 'herbivore')])

    @api.constrains('depredated', 'animalspe_ids')
    def _check_animals_are_carnivores_or_omnivores(self):
        for r in self:
            if not r.depredated and r.animalspe_ids:
                raise exceptions.ValidationError("error")


class Mineralspe(models.Model):
    _name = 'naturalparks.mineralspe'
    _inherit = 'naturalparks.species'
    _order = 'name'

    mineralspe_type = fields.Selection([('crystal', 'Crystal'), ('stone', 'Stone')], required=True)
    
from odoo import models, fields, api, exceptions

class Species(models.Model):
    _name = 'appnaturalparks.species'

    name = fields.Char(string="Binomial nomenclature", required=True)
    common_name = fields.Char(required=True)
    number_of_species = fields.Integer()

    area_ids = fields.Many2many('appnaturalparks.area', string="Area", required=True)

    class Vegetable(models.Model):
    _name = 'appnaturalparks.vegetable'
    _inherit = 'appnaturalparks.species'

    blooming = fields.Boolean(string="Does the plant have blooming?")
    blooming_period = fields.Selection([('spring', 'Spring'), ('summer', 'Summer'), ('autumn', 'Autumn'), ('winter', 'Winter')])
    is_eaten = fields.Boolean(string="Is this plant eaten?")
    
    animal_ids = fields.Many2many('appnaturalparks.animal', string="Herbivores which eat this plant", 
        domain=[('alimentation', '!=', 'carnivore')])

    @api.constrains('blooming', 'vegetable_blooming')
    def _check_vegetable_has_blooming(self):
        for v in self:
            if not v.blooming and v.vegetable_blooming:
                raise exceptions.ValidationError("Check if the vegetable has blooming before add the period")

    @api.constrains('eaten', 'animal_ids')
    def _check_animals_are_herbivores_or_omnivores(self):
        for a in self:
            if not a.eaten and a.animal_ids:
                raise exceptions.ValidationError("Check if the vegetable has been eaten before add the herbivores animals")
    
    class Animal(models.Model):
    _name = 'appnaturalparks.animal'
    _inherit = 'appnaturalparks.species'

    alimentation = fields.Selection([('carnivore','Carnivore'), ('herbivore','Herbivore'), ('omnivore','Omnivore')], required=True)
    mating_season = fields.Selection([('spring', 'Spring'), ('summer', 'Summer'), ('autumn', 'Autumn'), ('winter', 'Winter')])
    is_eaten = fields.Boolean(string="Is this animal eaten?")
    
    animal_ids = fields.Many2many(comodel_name='appnaturalparks.animal', relation='animals_eaten', column1='prey', column2='carnivores', string="Carnivores which eat this animal",
        domain=[('alimentation', '!=', 'herbivore')])
    
    @api.constrains('eaten', 'animal_ids')
    def _check_animals_are_carnivores_or_omnivores(self):
        for a in self:
            if not a.eaten and a.animal_ids:
                raise exceptions.ValidationError("Check eaten before the herbivores eating this vegetable")

    class Mineral(models.Model):
    _name = 'appnaturalparks.mineral'
    _inherit = 'appnaturalparks.species'

    mineral_type = fields.Selection([('crystal', 'Crystal'), ('stone', 'Stone')], required=True)
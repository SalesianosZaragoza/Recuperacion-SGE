from odoo import models

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

    class Animal(models.Model):
    _name = 'appnaturalparks.animal'
    _inherit = 'appnaturalparks.species'

    alimentation = fields.Selection([('carnivore','Carnivore'), ('herbivore','Herbivore'), ('omnivore','Omnivore')], required=True)
    mating_season = fields.Selection([('spring', 'Spring'), ('summer', 'Summer'), ('autumn', 'Autumn'), ('winter', 'Winter')])
    is_eaten = fields.Boolean(string="Is this animal eaten?")
    
    animal_ids = fields.Many2many(comodel_name='appnaturalparks.animal', relation='animals_eaten', column1='prey', column2='carnivores', string="Carnivores which eat this animal",
        domain=[('alimentation', '!=', 'herbivore')])

    class Mineral(models.Model):
    _name = 'appnaturalparks.mineral'
    _inherit = 'appnaturalparks.species'

    mineral_type = fields.Selection([('crystal', 'Crystal'), ('stone', 'Stone')], required=True)
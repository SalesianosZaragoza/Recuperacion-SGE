from odoo import models, fields, api, exceptions

class Species(models.Model):
    _name = 'ges.species'

    name = fields.Char(string="Cientific name", required=True)
    common_name = fields.Char(string="Common name", required=True)
    area_ids = fields.Many2many('ges.area', string="Area", required=True)
    areas_species_ids = fields.One2many(
        'ges.areas_species', 'specie_id', string="Especies")

class Vegetable(models.Model):
    _name = 'ges.vegetable'
    _inherit = 'ges.species'

    blooming = fields.Boolean(string="Florece?")
    blooming_period = fields.Selection([('spring', 'Spring'), ('summer', 'Summer'), ('autumn', 'Autumn'), ('winter', 'Winter')])

    is_eaten = fields.Boolean(string="La planta es comida?")
    animal_ids = fields.Many2many('ges.animal', string="Animales que comen esta planta", 
        domain=[('alimentation', '!=', 'carnivore')])

    @api.constrains('blooming', 'blooming_period')
    def _check_plant_has_blooming(self):
        for r in self:
            if not r.blooming and r.blooming_period:
                raise exceptions.ValidationError("Selecciona que la planta florece, si añades la estacion")

    @api.constrains('is_eaten', 'animal_ids')
    def _check_animals_are_herbivores_or_omnivores(self):
        for r in self:
            if not r.is_eaten and r.animal_ids:
                raise exceptions.ValidationError("Selecciona si la planta es comida, si añades animales carnivoros")

class Animal(models.Model):
    _name = 'ges.animal'
    _inherit = 'ges.species'

    alimentation = fields.Selection([('carnivore','Carnivore'), ('herbivore','Herbivore'), ('omnivore','Omnivore')], required=True)
    mating_season = fields.Selection([('spring', 'Spring'), ('summer', 'Summer'), ('autumn', 'Autumn'), ('winter', 'Winter')])

    is_eaten = fields.Boolean(string="Es este animal comido?")
    animal_ids = fields.Many2many(comodel_name='ges.animal', relation='animals_eaten', column1='prey', column2='carnivores', string="Animales que se comen a este animal",
        domain=[('alimentation', '!=', 'herbivore')])

    @api.constrains('is_eaten', 'animal_ids')
    def _check_animals_are_carnivores_or_omnivores(self):
        for r in self:
            if not r.is_eaten and r.animal_ids:
                raise exceptions.ValidationError("selecciona sin son comidos antes de señalar el animal")

class Mineral(models.Model):
    _name = 'ges.mineral'
    _inherit = 'ges.species'

    mineral_type = fields.Selection([('crystal', 'Crystal'), ('stone', 'Stone')], required=True)
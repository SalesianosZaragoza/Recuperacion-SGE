from odoo import models, fields, api, exceptions

class species(models.Model):
    _name = 'ges.species'

    name = fields.Char(string="Cientific name", required=True)
    common_name = fields.Char(string="Common name", required=True)
    areas_species_ids = fields.One2many(
        'ges.areas_species', 'species_id', string="Species")

class vegetable(models.Model):
    _name = 'ges.vegetable'
    _inherit = 'ges.species'

    blooming = fields.Boolean(string="Florece?")
    blooming_period = fields.Selection([('spring', 'Spring'), ('summer', 'Summer'), ('autumn', 'Autumn'), ('winter', 'Winter')])

    is_eaten = fields.Boolean(string="Is this vegetable eaten?")
    animal_ids = fields.Many2many('ges.animal', string="Animals that eat this vegetable", 
        domain=[('alimentation', '!=', 'carnivore')])

    @api.constrains('blooming', 'blooming_period')
    def _check_vegetable_has_blooming(self):
        for r in self:
            if not r.blooming and r.blooming_period:
                raise exceptions.ValidationError("Select that the vegetable blooms, if you select when")

    @api.constrains('is_eaten', 'animal_ids')
    def _check_animals_are_herbivores_or_omnivores(self):
        for r in self:
            if not r.is_eaten and r.animal_ids:
                raise exceptions.ValidationError("Select that the vegetable is eaten, if you select the animal")

class animal(models.Model):
    _name = 'ges.animal'
    _inherit = 'ges.species'

    alimentation = fields.Selection([('carnivore','Carnivore'), ('herbivore','Herbivore'), ('omnivore','Omnivore')], required=True)
    mating_season = fields.Selection([('spring', 'Spring'), ('summer', 'Summer'), ('autumn', 'Autumn'), ('winter', 'Winter')])

    is_eaten = fields.Boolean(string="Is this animal eaten?")
    animal_ids = fields.Many2many(comodel_name='ges.animal', relation='animals_eaten', column1='prey', column2='carnivores', string="Animales que se comen a este animal",
        domain=[('alimentation', '!=', 'herbivore')])

    @api.constrains('is_eaten', 'animal_ids')
    def _check_animals_are_carnivores_or_omnivores(self):
        for r in self:
            if not r.is_eaten and r.animal_ids:
                raise exceptions.ValidationError("Select that the vegetable is eaten, if you select the animal")

class mineral(models.Model):
    _name = 'ges.mineral'
    _inherit = 'ges.species'

    mineral_type = fields.Selection([('crystal', 'Crystal'), ('stone', 'Stone')], required=True)
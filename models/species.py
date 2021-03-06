from odoo import models, fields, api, exceptions

class species(models.Model):
    _name = 'odooIracema.species'

    name = fields.Char(string="Cientific name", required=True)
    common_name = fields.Char(string="Common name", required=True)
    areas_species_ids = fields.One2many(
        'odooIracema.areas_species', 'species_id', string="Species")

class vegetable(models.Model):
    _name = 'odooIracema.vegetable'
    _inherit = 'odooIracema.species'

    blooming = fields.Boolean(string="Florece?")
    blooming_period = fields.Selection([('spring', 'Spring'), ('summer', 'Summer'), ('autumn', 'Autumn'), ('winter', 'Winter')])

    is_eaten = fields.Boolean(string="Is this vegetable eaten?")
    animal_ids = fields.Many2many('odooIracema.animal', string="Animals that eat this vegetable", 
        domain=[('alimentation', '!=', 'carnivore')])
    
    @api.constrains('is_eaten', 'animal_ids')
    def _check_animals_are_herbivores_or_omnivores(self):
        for r in self:
            if not r.is_eaten and r.animal_ids:
                raise exceptions.ValidationError("Select that the vegetable is eaten, if you select the animal")

class animal(models.Model):
    _name = 'odooIracema.animal'
    _inherit = 'odooIracema.species'

    alimentation = fields.Selection([('carnivore','Carnivore'), ('herbivore','Herbivore'), ('omnivore','Omnivore')], required=True)
    mating_season = fields.Selection([('spring', 'Spring'), ('summer', 'Summer'), ('autumn', 'Autumn'), ('winter', 'Winter')])

    is_eaten = fields.Boolean(string="Is this animal eaten?")
    animal_ids = fields.Many2many(comodel_name='odooIracema.animal', relation='animals_eaten', column1='prey', column2='carnivores', string="Animales que se comen a este animal",
        domain=[('alimentation', '!=', 'herbivore')])
    
class mineral(models.Model):
    _name = 'odooIracema.mineral'
    _inherit = 'odooIracema.species'

    mineral_type = fields.Selection([('crystal', 'Crystal'), ('stone', 'Stone')], required=True)
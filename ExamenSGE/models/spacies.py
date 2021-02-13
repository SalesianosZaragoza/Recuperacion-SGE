from odoo import models, fields

class Species(models.Model):
    _name = 'naturalparks.species'

    name = fields.Char(string="Binomial nomenclature", required=True)
    common_name = fields.Char(required=True)
    area_ids = fields.Many2many('naturalparks.area', string="Area", required=True)
    number_of_specimens = fields.Integer()

class Plant(models.Model):
    _name = 'naturalparks.plant'
    _inherit = 'naturalparks.species'
    _order = 'name'

    growth = fields.Boolean(string="Does the plant have growth?")
    growth_period = fields.Selection([('spring', 'Spring'), ('summer', 'Summer'), ('autumn', 'Autumn'), ('winter', 'Winter')])

    eaten = fields.Boolean(string="eaten")
    animal_ids = fields.Many2many('naturalparks.animal', string="Herbivores", domain=[('alimentation', '!=', 'carnivore')])


class Animal(models.Model):
    _name = 'naturalparks.animal'
    _inherit = 'naturalparks.species'
    _order = 'name'

    alimentation = fields.Selection([('carnivore','Carnivore'), ('herbivore','Herbivore'), ('omnivore','Omnivore')], required=True)
    in_hot = fields.Selection([('spring', 'Spring'), ('summer', 'Summer'), ('autumn', 'Autumn'), ('winter', 'Winter')])
    color = fields.Integer()

    eaten = fields.Boolean(string="eaten")
    animal_ids = fields.Many2many(comodel_name='naturalparks.animal', relation='animals_eaten', column1='prey', column2='carnivores', string="Carnivores", domain=[('alimentation', '!=', 'herbivore')])

class Mineral(models.Model):
    _name = 'naturalparks.mineral'
    _inherit = 'naturalparks.species'
    _order = 'name'

    mineral = fields.Selection([('crystal', 'Crystal'), ('stone', 'Stone')], required=True)
    color = fields.Integer()
from odoo import models, fields

class Species(models.Model):
    _name = 'naturalP.species'

    name = fields.Char(string="Binomial nomenclature", required=True)
    common_name = fields.Char(required=True)
    area_ids = fields.Many2many('naturalP.area', string="Area", required=True)
    number_of_specimens = fields.Integer()

class Plant(models.Model):
    _name = 'naturalP.plant'
    _inherit = 'naturalP.species'
    _order = 'name'

    growth = fields.Boolean(string="Does the plant have growth?")
    growth_period = fields.Selection([('spring', 'Spring'), ('summer', 'Summer'), ('autumn', 'Autumn'), ('winter', 'Winter')])

    eaten = fields.Boolean(string="eaten")
    animal_ids = fields.Many2many('naturalP.animal', string="Herbivores", domain=[('alimentation', '!=', 'carnivore')])


class Animal(models.Model):
    _name = 'naturalP.animal'
    _inherit = 'naturalP.species'
    _order = 'name'

    alimentation = fields.Selection([('carnivore','Carnivore'), ('herbivore','Herbivore'), ('omnivore','Omnivore')], required=True)
    in_hot = fields.Selection([('spring', 'Spring'), ('summer', 'Summer'), ('autumn', 'Autumn'), ('winter', 'Winter')])
    color = fields.Integer()

    eaten = fields.Boolean(string="eaten")
    animal_ids = fields.Many2many(comodel_name='naturalP.animal', relation='animals_eaten', column1='prey', column2='carnivores', string="Carnivores", domain=[('alimentation', '!=', 'herbivore')])

class Mineral(models.Model):
    _name = 'naturalP.mineral'
    _inherit = 'naturalP.species'
    _order = 'name'

    mineral = fields.Selection([('crystal', 'Crystal'), ('stone', 'Stone')], required=True)
    color = fields.Integer()
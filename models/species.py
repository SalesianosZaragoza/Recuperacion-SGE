from odoo import models, fields

class Species(models.Model):
    _name = 'RecuperacionOdooCristianMarin.species'

    name = fields.Char(string="Name")
    common_name = fields.Char(string="Common Denomination")
    number_of_specimens = fields.Integer(string="number species")
    area_ids = fields.Many2many('RecuperacionOdooCristianMarin.area', string="Area")

class Plant(models.Model):
    _name = 'RecuperacionOdooCristianMarin.plant'
    _inherit = 'RecuperacionOdooCristianMarin.species'

    flowering = fields.Boolean(string="¿Florece la planta?")
    flowering_period = fields.Selection([('spring', 'spring'), ('summer', 'summer'), ('autumn', 'autum'), ('winter', 'winter')])
    is_eaten = fields.Boolean(string="¿Es comida?")
    animal_ids = fields.Many2many('RecuperacionOdooCristianMarin.animal', string="Animales que se comen esta planta")


class Animal(models.Model):
    _name = 'RecuperacionOdooCristianMarin.animal'
    _inherit = 'RecuperacionOdooCristianMarin.species'

    alimentation = fields.Selection([('carnivore','carnivore'), ('herbivore','herbivore'), ('omnivore','Omnivore')])
    mating_season = fields.Selection([('spring', 'spring'), ('summer', 'summer'), ('autumn', 'autum'), ('winter', 'winter')])

    is_eaten = fields.Boolean(string="¿Es una presa?")
    animal_ids = fields.Many2many(comodel_name='RecuperacionOdooCristianMarin.animal', relation='animals_eaten', column1='presa', column2='depredador')

class Mineral(models.Model):
    _name = 'RecuperacionOdooCristianMarin.mineral'
    _inherit = 'RecuperacionOdooCristianMarin.species'

    mineral_type = fields.Selection([('crystal', 'Crystal'), ('stone', 'stone')]) 
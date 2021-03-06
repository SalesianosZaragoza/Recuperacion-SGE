from odoo import models, fields

class Species(models.Model):
    _name = 'recu.species'

    name = fields.Char(string="Nombre cientifico")
    common_name = fields.Char(string="Nombre comun")
    number_of_specimens = fields.Integer(string="Numero de especies")
    area_ids = fields.Many2many('recu.area', string="Area")

class Plant(models.Model):
    _name = 'recu.plant'
    _inherit = 'recu.species'

    flowering = fields.Boolean(string="¿Florece la planta?")
    flowering_period = fields.Selection([('spring', 'Primavera'), ('summer', 'Verano'), ('autumn', 'Otoño'), ('winter', 'Invierno')])
    is_eaten = fields.Boolean(string="¿Es comida?")
    animal_ids = fields.Many2many('recu.animal', string="Animales que se comen esta planta")


class Animal(models.Model):
    _name = 'recu.animal'
    _inherit = 'recu.species'

    alimentation = fields.Selection([('carnivore','Carnivoros'), ('herbivore','Herbivoro'), ('omnivore','Omnivoro')])
    mating_season = fields.Selection([('spring', 'Primavera'), ('summer', 'Verano'), ('autumn', 'Otoño'), ('winter', 'Invierno')])

    is_eaten = fields.Boolean(string="¿Es una presa?")
    animal_ids = fields.Many2many(comodel_name='recu.animal', relation='animals_eaten', column1='presa', column2='depredador')

class Mineral(models.Model):
    _name = 'recu.mineral'
    _inherit = 'recu.species'

    mineral_type = fields.Selection([('crystal', 'Cristal'), ('stone', 'Piedra')]) 
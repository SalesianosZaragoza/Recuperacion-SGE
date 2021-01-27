from odoo import models, fields, api, exceptions

class Species(models.Model):
    _name = 'ges.species'

class Vegetable(models.Model):
    _name = 'ges.vegetable'
    _inherit = 'ges.species'

class Animal(models.Model):
    _name = 'ges.animal'
    _inherit = 'ges.species'

class Mineral(models.Model):
    _name = 'ges.mineral'
    _inherit = 'ges.species'
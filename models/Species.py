from odoo import models, fields, api

class Species(models.Model):
    _name = 'npi.Species'

    name = fields.Char(string="Scientific name", required=True)
    name = fields.Char(string="Vulgar name", required=True)
    numberSpecies = fields.Integer(string="Número de especies")


class Plant(models.Model):
    _name = 'npi.Plant'
    _inherit = 'npi.Species'

    floration = fields.Boolean(string="Does it have flowering?")
    florationPeriod = fields.Selection([(('winter', 'Winter'), ('spring', 'Spring'), ('summer', 'Summer'), ('autumn', 'Autumn'))])


class Animal(models.Model):
    _name = 'npi.Animal'
    _inherit = 'npi.Species'

    alimentation = fields.Selection([('carnivore', 'Carnivore'), ('herbivore', 'Herbivore'), ('omnivore', 'Omnivore')], required=True)
    reproductionPeriod = fields.Selection([('annual', 'Annual'), ('periodic', 'Periodic'), ('permanente', 'Permanente')], required=True)


class Mineral(models.Model):
    _name = 'npi.Mineral'
    _inherit = 'npi.Species'

    mineralType = fields.Selection([('glass', 'Glass'), ('rock', 'Rock')], required=True)
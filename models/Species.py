from odoo import models, fields, api

class species(models.Model):
    _name = 'npi.species'

    name = fields.Char(string="Scientific name", required=True)
    name = fields.Char(string="Vulgar name", required=True)
    numberSpecies = fields.Integer(string="Número de especies")

    area_ids = fields.Many2many('npi.area', string="Area", required=True)


class plant(models.Model):
    _name = 'npi.plant'
    _inherit = 'npi.species'

    floration = fields.Boolean(string="Does it have flowering?")
    florationPeriod = fields.Selection([(('winter', 'Winter'), ('spring', 'Spring'), ('summer', 'Summer'), ('autumn', 'Autumn'))])

    animal_ids = fields.Many2many('npi.animal', string="Animals that eat this plant", required=True)


class animal(models.Model):
    _name = 'npi.animal'
    _inherit = 'npi.species'

    alimentation = fields.Selection([('carnivore', 'Carnivore'), ('herbivore', 'Herbivore'), ('omnivore', 'Omnivore')], required=True)
    reproductionPeriod = fields.Selection([('annual', 'Annual'), ('periodic', 'Periodic'), ('permanente', 'Permanente')], required=True)


class mineral(models.Model):
    _name = 'npi.mineral'
    _inherit = 'npi.species'

    mineralType = fields.Selection([('glass', 'Glass'), ('rock', 'Rock')], required=True)
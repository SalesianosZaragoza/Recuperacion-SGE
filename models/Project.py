from odoo import models, fields, api

class project(models.Model):
    _name = 'npi.project'

    name = fields.Char(string="Name", required=True)
    budget = fields.Integer(string="Budget")
    realizationPeriod = fields.Selection([('in_process', 'In_process'), ('Done', 'Done'), ('coming_soon', 'Coming_soon')] string="Status")

    species_id = fields.Many2one('npi.species', string="Specie")
    investigator_ids = fields.Many2many('npi.investigator', string="Investigator/s")
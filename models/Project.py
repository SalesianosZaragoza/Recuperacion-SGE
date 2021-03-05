from odoo import models, fields, api

class project(models.Model):
    _name = 'npi.project'

    name = fields.Char(string="Name", required=True)
    budget = fields.Integer(string="Budget", required=True)
    realizationPeriod = fields.Selection([('in process', 'In process'), ('Done', 'Done'), ('coming soon', 'Coming soon')] string="Status")

    species_id = fields.Many2one('npi.species', string="Specie", required=True)
    investigator_ids = fields.Many2many('npi.investigator', string="Investigator/s", required=True)
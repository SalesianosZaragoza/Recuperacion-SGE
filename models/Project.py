from odoo import models, fields, api

class Project(models.Model):
    _name = 'npi.Project'

    name = fields.Char(string="Name", required=True)
    budget = fields.Integer(string="Budget", required=True)
    realizationPeriod = fields.Selection([('in process', 'In process'), ('Done', 'Done'), ('coming soon', 'Coming soon')] string="Status")

    Species_id = fields.Many2one('npi.Species', string="Specie", required=True)
    Investigator_ids = fields.Many2many('npi.Investigator', string="Investigator/s", required=True)
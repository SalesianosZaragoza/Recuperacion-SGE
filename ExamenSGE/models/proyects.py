from datetime import timedelta
from odoo import models, fields

class Project(models.Model):
    _name = 'naturalparks.project'
    _order = 'starting_date'

    name = fields.Char(string="Project Name", required=True)
    species_id = fields.Many2one('naturalparks.species', string="Species", required=True)
    research_ids = fields.Many2many('naturalparks.research', string="Researchers", required=True)
    budget = fields.Float(string="Budget", digits=(5, 3)
    starting_date = fields.Date(required=True)
    ending_date = fields.Date(required=True)
    color = fields.Integer()
    state = fields.Selection([('1.draft', 'Draft'), ('2.confirm', 'Confirm'), ('3.done', 'Done'), ], string='Status', default='1.draft')

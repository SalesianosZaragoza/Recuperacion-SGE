from datetime import timedelta
from odoo import models, fields

class Project(models.Model):
    _name = 'naturalP.project'
    _order = 'name'

    name = fields.Char(string="Project Name", required=True)
    species_id = fields.Many2one('naturalP.species', string="Species", required=True)
    research_ids = fields.Many2many('naturalP.research', string="Researchers", required=True)
    budget = fields.Float(string="Budget", digits=(5, 3)
    start_date = fields.Date(required=True)
    end_date = fields.Date(required=True)
    color = fields.Integer()
    state = fields.Selection([('1.draft', 'Draft'), ('2.confirm', 'Confirm'), ('3.done', 'Done'), ], string='Status', default='1.draft')

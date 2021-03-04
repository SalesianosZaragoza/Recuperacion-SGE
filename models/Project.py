from datetime import timedelta
from odoo import models, fields, api, exceptions

class Project(models.Model):
    _name = 'naturalparks.project'
    _order = 'starting_date'

    name = fields.Char(string="Project name", required=True)
    species_id = fields.Many2one('naturalparks.species', string="Species", required=True)
    researchper_ids = fields.Many2many('naturalparks.researchper', string="Researchers", required=True)
    budget = fields.Float(string="budget in dollars", digits=(8, 2))
    starting_date = fields.Date(required=True)
    ending_date = fields.Date(required=True)
    color = fields.Integer()
    state = fields.Selection([
            ('1.draft', 'Draft'),
            ('2.confirm', 'Confirm'),
            ('3.done', 'Done'),
        ], string='Status', default='1.draft')

    @api.constrains('budget')
    def _check_park_has_extension(self):
        for r in self:
            if r.budget <= 0:
                raise exceptions.ValidationError("error")

    @api.constrains('starting_date', 'ending_date')
    def _check_ending_date_is_after_starting_date(self):
        for r in self:
            if r.starting_date > r.ending_date:
                raise exceptions.ValidationError("error")

    def action_confirm(self):
        for r in self:
            r.state = '2.confirm'
            
    def action_done(self):
        for r in self:
            r.state = '3.done'

    def action_draft(self):
        for r in self:
            r.state = '1.draft'
    

    

    
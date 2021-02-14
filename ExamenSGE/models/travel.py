from odoo import models, fields
class Travel(models.Model):
    _name = 'naturalP.travel'
    _order = 'start_date'

    name = fields.Char(string="Travel", required=True)
    end_date = fields.Datetime(required=True)
    start_date = fields.Datetime(required=True)
    travel_type = fields.Selection([('car', 'Car'), ('walking', 'Walking')]) 
    natural_park_id = fields.Many2one('naturalP.natural_park', ondelete='cascade', string="Natural Park", required=True)
    acommodation_id = fields.Many2one('naturalP.acommodation', string="Acommodation", required=True)
    visitor_ids = fields.Many2many('naturalP.visitor', string="Visitors")
    total_visitors = fields.Integer(compute='_calculate_visitors')
    color = fields.Integer()
    state = fields.Selection([('1.draft', 'Draft'), ('2.confirm', 'Confirm'), ('3.done', 'Done'),], string='Status', default='1.draft')

    

    
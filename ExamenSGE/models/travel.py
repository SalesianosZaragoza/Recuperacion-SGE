from odoo import models, fields, api, exceptions
from odoo.exceptions import ValidationError

class Travel(models.Model):
    _name = 'naturalparks.travel'
    _order = 'starting_date'

    name = fields.Char(string="Travel", required=True)
    travel_type = fields.Selection([('car', 'Car'), ('walking', 'Walking')]) 
    start_date = fields.Datetime(required=True)
    end_date = fields.Datetime(required=True)
    natural_park_id = fields.Many2one('naturalparks.natural_park', ondelete='cascade', string="Natural Park", required=True)
    acommodation_id = fields.Many2one('naturalparks.acommodation', string="Acommodation", required=True)
    visitor_ids = fields.Many2many('naturalparks.visitor', string="Visitors")
    total_visitors = fields.Integer(compute='_calculate_visitors')
    color = fields.Integer()
    state = fields.Selection([('1.draft', 'Draft'), ('2.confirm', 'Confirm'), ('3.done', 'Done'),], string='Status', default='1.draft')

    

    
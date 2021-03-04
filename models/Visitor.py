from odoo import models, fields, api, exceptions

class Visitor(models.Model):
    _name = 'naturalparks.visitor'
    _order = 'name'

    name = fields.Char(string="visitor name", required=True)    
    dni = fields.Char(string="dni of the visitor", required=True)
    address = fields.Char(string="address of the visitor")
    job = fields.Char(string="job of the visitor")
    state = fields.Selection([
            ('1.draft', 'Draft'),
            ('2.confirm', 'Confirm'),
            ('3.done', 'Done'),
        ], string='Status', default='1.draft')

    natural_park_id = fields.Many2one('naturalparks.natural_park', string="Natural Park", ondelete='cascade', required=True)
    lodging_id = fields.Many2one('naturalparks.lodging', string="lodging", required=True)
    managementper_id = fields.Many2one('naturalparks.managementper', string="management employee responsible")


    def action_confirm(self):
        for r in self:
            r.state = '2.confirm'
            
    def action_done(self):
        for r in self:
            r.state = '3.done'

    def action_draft(self):
        for r in self:
            r.state = '1.draft'
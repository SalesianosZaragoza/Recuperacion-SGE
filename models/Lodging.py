from odoo import models, fields, api, exceptions

class Lodging(models.Model):
    _name = 'naturalparks.lodging'
    _order = 'name'

    name = fields.Char(string="name of the lodging", required=True)
    capacity = fields.Integer(string="capacity of the lodging",required=True)
    category = fields.Selection([('one', '*'), ('two','**'), ('three', '***'), ('four', '****'), ('five', '*****')])
    
    
    natural_park_id = fields.Many2one('naturalparks.natural_park', string="Natural Park", ondelete='cascade', required=True)

    @api.constrains('capacity')
    def _check_capacity_is_higher_than_zero(self):
        for r in self:
            if r.capacity <= 0:
                raise exceptions.ValidationError("error")

    

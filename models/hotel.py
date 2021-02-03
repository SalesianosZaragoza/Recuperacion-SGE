from odoo import models, fields, api, exceptions

class Hotel(models.Model):
    _name = 'appnaturalparks.hotel'

    name = fields.Char(string="Name", required=True)
    capacity = fields.Integer(required=True)
    category = fields.Selection([('one', 'one star'), ('two','two stars'), ('three', 'three stars'), ('four', 'four stars'), ('five', 'five stars')])

    natural_park_id = fields.Many2one('appnaturalparks.naturalpark', string="Natural Park", ondelete='cascade', required=True)

    @api.constrains('capacity')
    def _check_capacity_is_higher_than_zero(self):
        for h in self:
            if h.capacity <= 0:
                raise exceptions.ValidationError("The capacity must be higher than zero")


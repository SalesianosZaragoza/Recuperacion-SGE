from odoo import models, fields, api, exceptions

class Natural_Park(models.Model):
    _name = 'naturalP.natural_park'
    _order = 'name'

    name = fields.Char(string="Name", required=True)
    start_date = fields.Date()
    length = fields.Integer(string="length", required=True)

    community_ids = fields.Many2many('naturalP.community', string="CA", required=True)

    @api.constrains('length')
    def _length(self):
        for l in self:
            if l.length <= 0:
                raise exceptions.ValidationError("YOU NEED LENGTH")

    
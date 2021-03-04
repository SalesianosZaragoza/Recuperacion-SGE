from odoo import models, fields, api, exceptions

class Natural_park(models.Model):
    _name = 'naturalparks.natural_park'
    _order = 'name'

    name = fields.Char(string="name of the natural park", required=True)
    statement_date = fields.Date()
    extension = fields.Integer(string="kilometres of the natural park", required=True)

    community_ids = fields.Many2many('naturalparks.community', string="communities", required=True)

    @api.constrains('extension')
    def _check_park_has_extension(self):
        for r in self:
            if r.extension <= 0:
                raise exceptions.ValidationError("error")
   
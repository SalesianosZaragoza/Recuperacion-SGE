from odoo import models, fields, api, exceptions

class Community(models.Model):
    _name = 'naturalP.community'
    _order = 'name'

    name = fields.Char(string="Name", required=True)
    length = fields.Integer(string="length", required=True)
    administrative_authority = fields.Char(required=True)

    @api.constrains('length')
    def _length(self):
        for r in self:
            if r.length <= 0:
                raise exceptions.ValidationError("YOU NEED LENGTH")

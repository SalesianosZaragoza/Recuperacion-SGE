from odoo import models, fields, api, exceptions

class Community(models.Model):
    _name = 'naturalparks.community'
    _order = 'name'

    name = fields.Char(string="name of the community", required=True)
    extension = fields.Integer(string="kilometres of the community", required=True)
    responsible_org = fields.Char(string="responsible org", required=True)

    @api.constrains('extension')
    def _check_park_has_extension(self):
        for r in self:
            if r.extension <= 0:
                raise exceptions.ValidationError("error")
    
    
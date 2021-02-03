from odoo import models, fields, api, exceptions

class Community(models.Model):
    _name = 'appnaturalparks.community'
    
    name = fields.Char(string="Name", required=True)
    administrative_authority = fields.Char(required=True)
    extension = fields.Integer(string="Extension (in km2)", required=True)

    @api.constrains('extension')
    def _check_park_has_extension(self):
        for c in self:
            if c.extension <= 0:
                raise exceptions.ValidationError("The community must have a extension")

    
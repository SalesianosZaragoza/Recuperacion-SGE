from odoo import models, fields, api, exceptions

class Area(models.Model):
    _name = 'appnaturalparks.area'

    name = fields.Char(string="Name", required=True)
    extension = fields.Integer(string="Extension (in km2)", required=True)

    natural_park_id = fields.Many2one('appnaturalparks.naturalpark', string="Natural Park", ondelete='cascade', required=True)
    community_id = fields.Many2one('appnaturalparks.community', string="Community", required=True)

    @api.constrains('extension')
    def _check_park_has_extension(self):
        for a in self:
            if a.extension <= 0:
                raise exceptions.ValidationError("The area must have a extension")
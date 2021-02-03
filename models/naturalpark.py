from odoo import models, fields, api, exceptions

class NaturalPark(models.Model):
    _name = 'appnaturalparks.naturalpark'

    name = fields.Char(string="Name", required=True)
    starting_date = fields.Date()
    extension = fields.Integer(string="Extension (in km2)", required=True)
    
    community_ids = fields.Many2many('appnaturalparks.community', string="Communities Of Spain", required=True)

    @api.constrains('extension')
    def _check_park_has_extension(self):
        for n in self:
            if n.extension <= 0:
                raise exceptions.ValidationError("The natural park must have a extension")

    
from odoo import models

class Area(models.Model):
    _name = 'appnaturalparks.area'

    name = fields.Char(string="Name", required=True)
    extension = fields.Integer(string="Extension (in km2)", required=True)

    natural_park_id = fields.Many2one('appnaturalparks.naturalpark', string="Natural Park", ondelete='cascade', required=True)
    community_id = fields.Many2one('appnaturalparks.community', string="Community", required=True)
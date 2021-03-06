from odoo import models, fields, api, exceptions

class natural_Park(models.Model):
    _name = 'iracema.natural_park'

    name = fields.Char(string="Name", required=True)
    starting_date = fields.Date(required=True)
    autonomous_community_natural_park_ids = fields.One2many(
        'iracema.autonomous_community_natural_park', 'autonomous_community_id', string="Natural park")
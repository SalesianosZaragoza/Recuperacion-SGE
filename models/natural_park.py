from odoo import models, fields, api, exceptions

class Natural_Park(models.Model):
    _name = 'ges.natural_park'

    name = fields.Char(string="Name", required=True)
    starting_date = fields.Date(required=True)
    autonomous_community_natural_park_ids = fields.One2many(
        'ges.autonomous_community_natural_park', 'autonomous_community_id', string="Natural park")
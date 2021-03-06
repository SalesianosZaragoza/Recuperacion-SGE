from odoo import models, fields, api, exceptions

class natural_Park(models.Model):
    _name = 'odooIracema.natural_park'

    name = fields.Char(string="Name", required=True)
    starting_date = fields.Date(required=True)
    autonomous_community_natural_park_ids = fields.One2many(
        'odooIracema.autonomous_community_natural_park', 'autonomous_community_id', string="Natural park")
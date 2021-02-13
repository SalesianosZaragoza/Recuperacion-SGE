from odoo import models, fields

class Area(models.Model):
    _name = 'naturalP.area'
    _order = 'natural_park_id'

    name = fields.Char(string="Name", required=True)
    length = fields.Integer(string="length", required=True)

    natural_park_id = fields.Many2one('naturalP.natural_park', string="Natural Park", ondelete='cascade', required=True)
    community_id = fields.Many2one('naturalP.community', string="Community", required=True)

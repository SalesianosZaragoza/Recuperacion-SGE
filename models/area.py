from odoo import models, fields, api, exceptions

class Area(models.Model):
    _name = 'odoonp.area'

    name = fields.Char(string="Nombre")
    extension = fields.Integer(string="Extension")
    community_id = fields.Many2one('odoonp.community', string="community") 
    natural_park_id = fields.Many2one('odoonp.natural_park', string="Natural Park")


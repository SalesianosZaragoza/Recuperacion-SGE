from odoo import models, fields, api, exceptions

class Area(models.Model):
    _name = 'RecuperacionOdooCristianMarin.area'

    name = fields.Char(string="Nombre")
    extension = fields.Integer(string="Extension")
    community_id = fields.Many2one('RecuperacionOdooCristianMarin.community', string="community") 
    natural_park_id = fields.Many2one('RecuperacionOdooCristianMarin.natural_park', string="Natural Park")


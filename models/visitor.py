from odoo import models

class Visitor(models.Model):
    _name = 'appnaturalparks.visitor'

    name = fields.Char(required=True)    
    dni = fields.Char(required=True)
    address = fields.Char()
    job = fields.Char()

    natural_park_id = fields.Many2one('appnaturalparks.natural_park', string="Natural Park", ondelete='cascade', required=True)
    hotel_id = fields.Many2one('appnaturalparks.hotel', string="Hotel", required=True)
    management_id = fields.Many2one('appnaturalparks.management', string="Person who registered this visitor")
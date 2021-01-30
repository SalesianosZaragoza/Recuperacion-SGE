from odoo import models

class Excursion(models.Model):
    _name = 'appnaturalparks.excursion'

    name = fields.Char(string="Definition of the excursion", required=True)
    trip_type = fields.Selection([('car', 'Car'), ('walking', 'Walking')]) 
    starting_date = fields.Datetime(required=True)
    ending_date = fields.Datetime(required=True)

    natural_park_id = fields.Many2one('appnaturalparks.natural_park', ondelete='cascade', string="Natural Park", required=True)
    hotel_id = fields.Many2one('appnaturalparks.hotel', string="Hotel Organizer", required=True)
    visitor_ids = fields.Many2many('appnaturalparks.visitor', string="Visitors")
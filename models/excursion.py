from odoo import models, fields, api, exceptions

class Excursion(models.Model):
    _name = 'appnaturalparks.excursion'

    name = fields.Char(string="Definition of the excursion", required=True)
    excursion_type = fields.Selection([('car', 'Car'), ('walking', 'Walking')]) 
    starting_date = fields.Datetime(required=True)
    ending_date = fields.Datetime(required=True)

    natural_park_id = fields.Many2one('appnaturalparks.natural_park', ondelete='cascade', string="Natural Park", required=True)
    hotel_id = fields.Many2one('appnaturalparks.hotel', string="Hotel Organizer", required=True)
    visitor_ids = fields.Many2many('appnaturalparks.visitor', string="Visitors")

    @api.onchange('natural_park_id')
    def onchange_natural_park_id_check_hotel(self):
        for e in self:
            return {
                'warning': {
                'title': "Something bad happened",
                'message': "You have to check the hotel",
                }
            }
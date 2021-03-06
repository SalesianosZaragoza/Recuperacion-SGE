from odoo import models, fields

class Trip(models.Model):
    _name = 'odoonp.trip'

    name = fields.Char(string="Excursion")
    trip_type = fields.Selection([('walking', 'Andando'), ('car', 'Coche')]) 
    trip_starting = fields.Datetime( string="Fecha salida")
    trip_ending = fields.Datetime( string="Fecha llegada")
    acommodation_id = fields.Many2one('odoonp.acommodation', ondelete='cascade', string="Acommodation") 
    natural_park_id = fields.Many2one('odoonp.natural_park', string="Natural Park")
    visitor_ids = fields.Many2many('odoonp.visitor', string="Visitors") 
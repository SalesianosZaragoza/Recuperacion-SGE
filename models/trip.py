from odoo import models, fields

class Trip(models.Model):
    _name = 'recu.trip'

    name = fields.Char(string="Excursion")
    trip_type = fields.Selection([('walking', 'Andando'), ('car', 'Coche')]) 
    trip_starting = fields.Datetime( string="Fecha salida")
    trip_ending = fields.Datetime( string="Fecha llegada")
    acommodation_id = fields.Many2one('recu.acommodation', ondelete='cascade', string="Alojamineto") 
    natural_park_id = fields.Many2one('recu.natural_park', string="Parque natural")
    visitor_ids = fields.Many2many('recu.visitor', string="Visitantes") 

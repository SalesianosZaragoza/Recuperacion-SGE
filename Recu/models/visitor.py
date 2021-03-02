from odoo import models, fields, api

class Visitor(models.Model):
    _name = 'recu.visitor'

    dni = fields.Char()
    name = fields.Char()
    address = fields.Char()
    work = fields.Char()

    management_id = fields.Many2one('recu.management', string="Gestion del parque") 
    acommodation_id = fields.Many2one('recu.acommodation', ondelete='cascade', string="Alojamiento") 
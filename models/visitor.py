from odoo import models, fields

class Visitor(models.Model):
    _name = 'RecuperacionOdooCristianMarin.visitor'

    dni = fields.Char()
    name = fields.Char()
    address = fields.Char()
    work = fields.Char()

    management_id = fields.Many2one('RecuperacionOdooCristianMarin.management', string="Park management") 
    acommodation_id = fields.Many2one('RecuperacionOdooCristianMarin.acommodation', ondelete='cascade', string="Acommodation") 
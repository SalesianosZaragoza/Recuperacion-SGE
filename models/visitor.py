from odoo import models, fields

class Visitor(models.Model):
    _name = 'odoonp.visitor'

    dni = fields.Char()
    name = fields.Char()
    address = fields.Char()
    work = fields.Char()

    management_id = fields.Many2one('odoonp.management', string="Park management") 
    acommodation_id = fields.Many2one('odoonp.acommodation', ondelete='cascade', string="Acommodation") 
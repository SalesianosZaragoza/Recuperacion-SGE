from odoo import models

class Hotel(models.Model):
    _name = 'appnaturalparks.hotel'

    name = fields.Char(string="Name", required=True)
    capacity = fields.Integer(required=True)
    category = fields.Selection([('one', '*'), ('two','**'), ('three', '***'), ('four', '****'), ('five', '*****')])

    natural_park_id = fields.Many2one('appnaturalparks.naturalpark', string="Natural Park", ondelete='cascade', required=True)
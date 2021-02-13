from odoo import models, fields

class Natural_Park(models.Model):
    _name = 'naturalP.natural_park'
    _order = 'name'

    name = fields.Char(string="Name", required=True)
    start_date = fields.Date()
    length = fields.Integer(string="length", required=True)

    community_ids = fields.Many2many('naturalP.community', string="Autonomies", required=True)

    
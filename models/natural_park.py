from odoo import models, fields

class Natural_Park(models.Model):
    _name = 'recu.natural_park'

    name = fields.Char(string="Nombre")
    starting_date = fields.Date(string="Fecha")
    extension = fields.Integer(string="Extension")

    community_ids = fields.Many2many('recu.community', string="Comunidad Autonoma") 
from odoo import models, fields

class parquenatural(models.Model):
    _name = 'np.parquenatural'

    name = fields.Char(string="nombre", required=True)
    starting_date = fields.Date()
    extension = fields.Integer(string="extension", required=True)

    comunidad_ids = fields.Many2many('np.comunidad', string="Comunidad autonoma", required=True)

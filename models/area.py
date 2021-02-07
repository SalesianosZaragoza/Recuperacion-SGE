from odoo import models, fields

class area(models.Model):
    _name = 'np.area'
    _order = 'parquenatural.id'

    name = fields.Char(string="nombre", required=True)
    extension = fields.Integer(string="extension", required=True)

    parquenatural.id = fields.Many2one('np.parquenatural', string="parque natural", ondelete='cascade', required=True)
    comunidad.id = fields.Many2one('np.comunidad', string="comunidad", required=True)

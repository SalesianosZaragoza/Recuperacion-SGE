from odoo import models, fields
class alojamiento(models.Model):
    _name = 'np.alojamiento'

    nombre = fields.Char(string="Name", required=True)
    capacidad = fields.Integer(required=True)
    categoria = fields.Selection([('A'), ('B'), ('C')])
    color = fields.Integer()
    
    parquenatural.id = fields.Many2one('np.parquenatural', string="Parque natural", ondelete='cascade', required=True)


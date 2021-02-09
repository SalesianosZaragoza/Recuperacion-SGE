from odoo import models, fields

class visitante(models.Model):
    _name = 'np.visitante'

    nombre = fields.Char(required=True)    
    dni = fields.Char(required=True)
    domicilio = fields.Char()
    profesion = fields.Char()
    color = fields.Integer()

    parquenatural.id = fields.Many2one('np.parquenatural', string="parque natural", ondelete='cascade', required=True)
    alojamiento.id = fields.Many2one('np.alojamiento', string="alojamiento", required=True)
    administracion.id = fields.Many2one('np.administracion', string="Registro del visitante")

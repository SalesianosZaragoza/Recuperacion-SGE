from odoo import models, fields


class excursiones(models.Model):
    _name = 'np.excursiones'


    nombre = fields.Char(string="excursiones", required=True)
    tExcursiones = fields.Selection([('a pie', 'a pie'), ('en vehiculo', 'en vehiculo')]) 
    diaSemana = fields.Datetime(required=True)
    horaDia = fields.Datetime(required=True)
    color = fields.Integer()

    parquenatural.id = fields.Many2one('np.parquenatural', ondelete='cascade', string="parque natural", required=True)
    alojamiento.id = fields.Many2one('np.alojamiento', string="alojamiento", required=True)
    visitante.id = fields.Many2many('np.visitante', string="visitante")

    


    
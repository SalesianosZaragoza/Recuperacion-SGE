from odoo import models, fields

class proyecto(models.Model):
    _name = 'np.proyecto'


    nombre = fields.Char(string="nombre", required=True)
    especies.id = fields.Many2one('np.especies', string="especies", required=True)
    investigador.id = fields.Many2many('np.investigador', string="investigadores", required=True)
    presupuesto = fields.Float(string="presupuesto")
    DiaComienzo = fields.Date(required=True)
    DiaFinal = fields.Date(required=True)
    color = fields.Integer()
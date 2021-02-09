from odoo import models, fields

class personal(models.Model):
    _name = 'np.personal'

    nombre = fields.Char(string="nombre", required=True)
    dni = fields.Char(required=True)
    nSeguridadSocial = fields.Char(required=True)
    parquenatural.id = fields.Many2one('np.parquenatural', ondelete='cascade', string="Parque natural", required=True)
    direccion = fields.Char()
    tlfn = fields.Char()
    tlfnDomicilio = fields.Char()
    salario = fields.Integer(string="salario")

class gestion(models.Model):
    _name = 'np.gestion'
    _inherit = 'np.personal'

    nEntrada = fields.Integer()

class vigilancia(models.Model):
    _name = 'np.vigilancia'
    _inherit = 'np.personal'

    area.id = fields.Many2one('np.area', string="area", required=True)
    coche.id = fields.Many2one('np.coche', string="coche", required=True)

class coche(models.Model):
    _name = 'np.coche'

    nombre = fields.Char(string="coche", required=True)
    matricula = fields.Char(string="matricula")
    color = fields.Integer()


class investigador(models.Model):
    _name = 'np.investigador'
    _inherit = 'np.personal'

    titulo = fields.Char(required=True)

class conservacion(models.Model):
    _name = 'np.conservacion'
    _inherit = 'np.personal'

    area.id = fields.Many2one('np.area', string="area", required=True)
    especialidad = fields.Selection([('limpieza', 'limpieza'), ('caninos', 'caninos')]) 

from odoo import models, fields

class comunidad(models.Model):
    _name = 'np.comunidad'


    nombre = fields.Char(string="nombre", required=True)
    extension = fields.Integer(string="extension", required=True)
    responsable = fields.Char(required=True)
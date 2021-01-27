from odoo import models

class Species(models.Model):
    _name = 'appnaturalparks.species'

    name = fields.Char(string="Binomial nomenclature", required=True)
    common_name = fields.Char(required=True)
    number_of_specimens = fields.Integer()
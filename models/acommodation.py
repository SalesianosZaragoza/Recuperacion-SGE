
from odoo import models, fields, api, exceptions
import random
from random import randint
import string

class Acommodation(models.Model):
    _name = 'recu.acommodation'

    name = fields.Char(string="Nombre")
    capacity = fields.Integer(string="Capacidad")
    category = fields.Selection([('uno', 'uno'), ('dos','dos'), ('tres', 'tres'), ('cuatro', 'cuatro'), ('cinco', 'cinco')],string="categoria") 
    natural_park_id = fields.Many2one('recu.natural_park', string="Parque natural")
    color = fields.Integer()

    @api.one
    def generate_record_name(self):
        self.write({'name': ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(randint(9,15)))})


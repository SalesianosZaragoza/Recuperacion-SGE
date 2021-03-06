from odoo import models, fields
import random
from random import randint
import string

class Acommodation(models.Model):
    _name = 'RecuperacionOdooCristianMarin.acommodation'

    name = fields.Char(string="Nombre")
    capacity = fields.Integer(string="Capacidad")
    category = fields.Selection([('ONE', '*'), ('TWO','**'), ('THREE', '***'), ('FOUR', '****'), ('FIVE', '*****')],string="category") 
    natural_park_id = fields.Many2one('RecuperacionOdooCristianMarin.natural_park', string="natural park")
    color = fields.Integer()

    def random_register(self):
        self.write({'name': ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(randint(9,15)))})


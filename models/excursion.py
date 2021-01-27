from odoo import models

class Excursion(models.Model):
    _name = 'appnaturalparks.excursion'

    name = fields.Char(string="Definition of the excursion", required=True)
    trip_type = fields.Selection([('car', 'Car'), ('walking', 'Walking')]) 
    starting_date = fields.Datetime(required=True)
    ending_date = fields.Datetime(required=True)
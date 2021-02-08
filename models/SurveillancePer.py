from odoo import models, fields, 

class SurveillancePer(models.Model):
    _name='NaturalParks.SurveillancePer'
    _order='name'


    Name = fields.Char(string="name of the community")
    Responsible_Org = fields.Char(string="name of the responsible org")
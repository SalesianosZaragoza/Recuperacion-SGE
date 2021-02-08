from odoo import models, fields, 

class ConservationPer(models.Model):
    _name='NaturalParks.ConservationPer'
    _order='name'


    Name = fields.Char(string="name of the community")
    Responsible_Org = fields.Char(string="name of the responsible org")
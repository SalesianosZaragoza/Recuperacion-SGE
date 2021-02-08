from odoo import models, fields, 

class Community(models.Model):
    _name='NaturalParks.Community'
    _order='name'


    Name = fields.Char(string="name of the community")
    Responsible_Org = fields.Char(string="name of the responsible org")
    
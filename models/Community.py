from odoo import models, fields, 

class Community(models.Model):
    _name='NaturalParks.Community'
    _order='name'


    Name = fields.Char()
    Responsible_Org = fields.Char()
    Extension = fields.Integer()
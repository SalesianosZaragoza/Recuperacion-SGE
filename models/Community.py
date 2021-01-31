from odoo import models, fields, api, exceptions

class Community(models.Model):
    _name='NaturalParks.Community'
    _order='name'


    Name = fields.Char(string="Name", required=True)
    Responsible_Org = fields.Char(required=True)
    Extension =
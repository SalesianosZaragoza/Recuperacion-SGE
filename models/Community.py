from odoo import models, fields, api

class Community(models.Model):
    _name='NaturalParks.Community'
    _order='Name'


    Name = fields.Char(string="name of the community")
    ResponsibleOrg = fields.Char(string="name of the responsible org")
    Extension = fields.Integer(string="kilometres")

    @api.constrains('Extension')
    
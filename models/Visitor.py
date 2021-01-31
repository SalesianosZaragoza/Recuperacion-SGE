from odoo import models, fields, api, exceptions

class Visitor(models.Model):
    _name='NaturalParks.Visitor'



    Name = fields.Char(string="Name", required=True)
    DNI = fields.Char(required=True)
    Address = fields.Char()
    Job = fields.Char()
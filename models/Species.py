from odoo import models, fields, api, exceptions

class Species(models.Model):
    _name='NaturalParks.Species'



    Name = fields.Char(string="Scientific Name", required=True)
    Species_Type =
    Vulgar_Name = fields.Char(required=True)
    Species_ID =
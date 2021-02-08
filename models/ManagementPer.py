from odoo import models, fields, 

class ManagementPer(models.Model):
    _name='NaturalParks.ManagementPer'
    _order='name'


    Name = fields.Char(string="name of the community")
    Responsible_Org = fields.Char(string="name of the responsible org")
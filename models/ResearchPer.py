from odoo import models, fields, 

class ResearchPer(models.Model):
    _name='NaturalParks.ResearchPer'
    _order='name'


    Name = fields.Char(string="name of the community")
    Responsible_Org = fields.Char(string="name of the responsible org")
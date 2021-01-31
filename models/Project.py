from odoo import models, fields, api

class Project(models.Model):
    _name = 'npi.Project'

    name = fields.Char(string="Name", required=True)
    budget = fields.Integer(string="Budget", required=True)
    realizationPeriod = fields.Selection([('in process', 'In process'), ('Done', 'Done'), ('coming soon', 'Coming soon')] string="Status")
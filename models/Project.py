from odoo import models, fields, api


class Project(models.Model):
    _name = 'NaturalParks.Project'
    _order = 'Name'

    Name = fields.Char(string="Project Name")
    ResearchPerID = fiels Many2many('NaturalParks.ResearchPer')
    Budget = fields.Float(string="Budget in dollars", digits=(9, 1))
    StartingDate = fields.Date()
    EndingDate = fields.Date()
    
    

    SpeciesID = fields.Many2one('naturalparks.Species', string="Species")


    @api.constrains('Budget')

    @api.constrains('StartingDate','EndingDate')
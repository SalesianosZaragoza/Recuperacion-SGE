from odoo import models, fields, api, exceptions


class Project(models.Model):
    _name = 'NaturalParks.Project'
    _order = 'name'

    name = fields.Char(string="Project Name")
    ResearchPerIDS = fields.Many2many('NaturalParks.ResearchPer')
    Budget = fields.Float(string="Budget in dollars", digits=(9, 1))
    StartingDate = fields.Date()
    EndingDate = fields.Date()
    Color = fields.Integer()
    State = fields.Selection([
        ('draft', 'Draft')
        ,('confirm', 'Confirm')
        ,('done', 'Done')
    ], default='draft')
    

    SpeciesID = fields.Many2one('NaturalParks.Species', string="Species")


    @api.constrains('Budget')
    def _How_Much_Budget_Has_The_Project(self):
        for r in self:
            if r.Budget <= 0:
                raise exceptions.ValidationError("error")

    @api.constrains('StartingDate','EndingDate')
    def _Is_The_Date_Correct(self):
        for r in self:
            if r.StartingDate > r.EndingDate:
                raise exceptions.ValidationError("error")
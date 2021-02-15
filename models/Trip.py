from odoo import models, fields, api, exceptions
from odoo.exceptions import ValidationError

class Trip(models.Model):
    _name='NaturalParks.Trip'
    
    


    name = fields.Char(string="name of the trip")
    TripType = fields.Selection([('car trip'), ('walk trip')]) 
    StartingDate = fields.Datetime()
    EndingDate = fields.Datetime()



    NaturalParkID = fields.Many2one('NaturalParks.NaturalPark')
    VisitorIDS = fields.Many2many('NaturalParks.Visitor')
    LodgingID = fields.Many2one('NaturalParks.Lodging')


    @api.constrains('NaturalParkID','VisitorIDS')
    def _Are_Visitors_In_The_NaturalPark(self):
        for r in self:
            if r.VisitorID.NaturalParkID != r.NaturalParkID and len(r.VisitorID) > 0:
                raise exceptions.ValidationError("error")

    @api.constrains('StartingDate','EndingDate')
    def _Is_The_Date_Correct(self):
        for r in self:
            if r.StartingDate > r.EndingDate:
                raise exceptions.ValidationError("error")

    
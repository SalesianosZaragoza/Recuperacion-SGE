from odoo import models, fields, api

class Trip(models.Model):
    _name='NaturalParks.Trip'
    _order='Name'
    


    Name = fields.Char(string="name of the trip")
    TripType = fields.Selection([('car trip'), ('walk trip')]) 
    StartingDate = fields.Datetime()
    EndingDate = fields.Datetime()



    NaturalParkID = fields.Many2one('NaturalParks.NaturalPark')
    VisitorID = fieldsMany2many('NaturalParks.Visitor')
    LodgingID = fields.Many2one('NaturalParks.Lodging')


    @api.constrains('NaturalParkID','VisitorID')

    @api.constrains('StartingDate','EndingDate')

    
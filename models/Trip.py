from odoo import models, fields, 

class Trip(models.Model):
    _name='NaturalParks.Trip'
    


    Name = fields.Char()
    Trip_Type = fields.Selection 
    Starting_Date = fields.Datetime
    Ending_Date = fields.Datetime



    NaturalParkID = fields.Many2one('NaturalParks.NaturalPark')
    VisitorID = fieldsMany2many('NaturalParks.Visitor')
    LodgingID = fields.Many2one('NaturalParks.Lodging')

    
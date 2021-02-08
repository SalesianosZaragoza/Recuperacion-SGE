from odoo import models, fields, 

class Trip(models.Model):
    _name='NaturalParks.Trip'
    


    Name = fields.Char(string="name of the trip")
    Trip_Type = fields.Selection([('car trip'), ('walk trip')]) 
    Starting_Date = fields.Datetime()
    Ending_Date = fields.Datetime()



    NaturalParkID = fields.Many2one('NaturalParks.NaturalPark')
    VisitorID = fieldsMany2many('NaturalParks.Visitor')
    LodgingID = fields.Many2one('NaturalParks.Lodging')

    
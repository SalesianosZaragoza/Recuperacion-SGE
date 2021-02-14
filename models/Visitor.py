from odoo import models, fields 

class Visitor(models.Model):
    _name='NaturalParks.Visitor'
    _order='name'



    name = fields.Char(string="name of the visitor")
    DNI = fields.Char(string="DNI of the visitor")
    Address = fields.Char(string="address of the visitor")
    Job = fields.Char(string="job of the visitor")


    LodgingID = fields.Many2one('NaturalParks.Lodging')
    NaturalParkID = fields.Many2one('NaturalParks.NaturalPark')
    ManagementPersID = fields.Many2one('NaturalParks.ManagementPers')
from odoo import models, fields, api, exceptions 
from odoo.exceptions import ValidationError
class Visitor(models.Model):
    _name='NaturalParks.Visitor'
    ss



    name = fields.Char(string="name of the visitor")
    DNI = fields.Char(string="DNI of the visitor")
    Address = fields.Char(string="address of the visitor")
    Job = fields.Char(string="job of the visitor")
    State = fields.Selection([
            ('1.draft', 'Draft'),
            ('2.confirm', 'Confirm'),
            ('3.done', 'Done'),
        ], string='Status', default='1.draft')


    LodgingID = fields.Many2one('NaturalParks.Lodging')
    NaturalParkID = fields.Many2one('NaturalParks.NaturalPark')
    ManagementPersID = fields.Many2one('NaturalParks.ManagementPers')
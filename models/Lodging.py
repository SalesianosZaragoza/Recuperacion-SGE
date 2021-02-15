from odoo import models, fields, api, exceptions
from odoo.exceptions import ValidationError
class Lodging(models.Model):
    _name='NaturalParks.Lodging'
    



    name = fields.Char(string="name of the lodging")
    Capacity = fields.Integer(string="capacity of the lodging")
    Category = fields.Selection([('One', '*'), ('Two','**'), ('Three', '***'), ('Four', '****'), ('Five', '*****')])
    


    NaturalParkID = fields.Many2one('NaturalParks.NaturalPark')

    @api.constrains('Capacity')
    def _Is_Capacity_Available(self):
        for r in self:
            if r.Capacity <= 0:
                raise exceptions.ValidationError("error")

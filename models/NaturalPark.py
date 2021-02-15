from odoo import models, fields, api, exceptions
from odoo.exceptions import ValidationError
class NaturalPark(models.Model):
    _name='NaturalParks.NaturalPark'
    



    name = fields.Char(string="name of the natural park")
    StatementDate = fields.Date()
    Extension = fields.Integer()
    

    CommunityIDS = fields.Many2many('NaturalParks.Community')

    @api.constrains('Extension')
    def _How_Much_Extension_Is_NaturalPark(self):
        for r in self:
            if r.Extension <= 0:
                raise exceptions.ValidationError("error")
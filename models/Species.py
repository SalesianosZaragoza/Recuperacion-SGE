from odoo import models, fields, api, exceptions

class Species(models.Model):
    _name='NaturalParks.Species'
    _order='name'



    name = fields.Char(string="name of the species")
    VulgarName = fields.Char(string="vulgar name of the species")
    NumberOfSpecimens = fields.Integer()


    AreaIDS = fields.Many2many('NaturalParks.Area')


    @api.constrains('NumberOfSpecimens')
    def _Is_The_Species_Here(self):
        for r in self:
            if r.NumberOfSpecimens <= 0:
                raise exceptions.ValidationError("error")
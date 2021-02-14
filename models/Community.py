from odoo import models, fields, api, exceptions

class Community(models.Model):
    _name='NaturalParks.Community'
    _order='name'


    name = fields.Char(string="name of the community")
    ResponsibleOrg = fields.Char(string="name of the responsible org")
    Extension = fields.Integer(string="kilometres")

    @api.constrains('Extension')
    def _How_Much_Extension_Is_NaturalPark(self):
        for r in self:
            if r.Extension <= 0:
                raise exceptions.ValidationError("error")
    
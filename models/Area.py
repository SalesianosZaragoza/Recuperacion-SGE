from odoo import models, fields, api, exceptions

class Area(models.Model):
    _name='NaturalParks.Area'
    _order='name'



    name = fields.Char(string="name of the area")
    Extension = fields.Integer(string="kilometres")
    
    NaturalParkID = fields.Many2one('NaturalParks.NaturalPark')
    CommunityID = fields.Many2one('NaturalParks.Community')

    @api.constrains('Extension')
    def _How_Much_Extension_Is_NaturalPark(self):
        for r in self:
            if r.Extension <= 0:
                raise exceptions.ValidationError("error")

    @api.constrains('NaturalParkID', 'CommunityID')
    def _What_community_Is_In_NaturalPark(self):
        for r in self:
            if r.CommunityID not in r.NaturalParkID.CommunityID:
                raise exceptions.ValidationError("error")

    
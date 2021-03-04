
from odoo import models, fields, api, exceptions

class Area(models.Model):
    _name = 'recu.area'

    name = fields.Char(string="Nombre")
    extension = fields.Integer(string="Extension")
    community_id = fields.Many2one('recu.community', string="Comunidad") 
    natural_park_id = fields.Many2one('recu.natural_park', string="Parque Natural")

    @api.constrains('natural_park_id', 'community_id')
    def _park_inside_community(self):
        for n in self:
            if n.community_id not in n.natural_park_id.community_ids:
                raise exceptions.ValidationError("En esta comunidad no esta el parque") 




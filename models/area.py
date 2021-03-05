from odoo import models, fields, api, exceptions

class area(models.Model):
    _name = 'npi.area'

    name = fields.Char(string="Name", required=True)
    extension = fields.Integer(string="Extension", required=True)

    naturalPark_id = fields.Many2one('npi.naturalPark', string="Natural Park")
    ca_id = fields.Many2one('npi.ca', string="Autonomous community")

    @api.constrains('naturalPark_id', 'ca_id')
    def _park_inside_community(self):
        for n in self:
            if n.ca_id not in n.naturalPark_id.ca_ids:
                raise exceptions.ValidationError("En esta comunidad no esta el parque") 
from odoo import models, fields, api, exceptions

class autonomous_Community(models.Model):
    _name = 'odooIracema.autonomous_community'

    name = fields.Char(string="Comunity", required=True)
    responsible_entity = fields.Char(string="Name of responsible entity", required=True)
    
    autonomous_community_natural_park_ids = fields.One2many(
        'odooIracema.autonomous_community_natural_park', 'autonomous_community_id', string="Natural park")

class autonomous_Community_Natural_Park(models.Model):
    _name = 'odooIracema.autonomous_community_natural_park'

    autonomous_community_id = fields.Many2one('odooIracema.autonomous_community',
        ondelete='set null', string="Comunidad Autonoma")
    natural_park_id = fields.Many2one('odooIracema.natural_park',
        ondelete='set null', string="Natural park")

    extension = fields.Integer(string="Extension (in km2)", required=True)

    @api.constrains('extension')
    def _check_park_has_extension(self):
        for r in self:
            if r.extension <= 0:
                raise exceptions.ValidationError("The extension must be grater than zero")
  
from odoo import models, fields, api, exceptions

class Autonomous_Community(models.Model):
    _name = 'ges.autonomous_community'

    name = fields.Char(string="Comunidad", required=True)
    responsible_entity = fields.Char(string="Nombre de entidad responsable", required=True)
    
    autonomous_community_natural_park_ids = fields.One2many(
        'ges.autonomous_community_natural_park', 'autonomous_community_id', string="Parques naturales")

class Autonomous_Community_Natural_Park(models.Model):
    _name = 'ges.autonomous_community_natural_park'

    autonomous_community_id = fields.Many2one('ges.autonomous_community',
        ondelete='set null', string="Comunidad Autonoma")
    natural_park_id = fields.Many2one('ges.natural_park',
        ondelete='set null', string="Parque natural")

    extension = fields.Integer(string="Extension (en km2)", required=True)

    @api.constrains('extension')
    def _check_park_has_extension(self):
        for r in self:
            if r.extension <= 0:
                raise exceptions.ValidationError("La extensión no puede ser 0")
  
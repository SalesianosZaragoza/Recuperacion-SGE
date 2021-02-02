from odoo import models, fields, api, exceptions

class Areas(models.Model):
    _name = 'ges.areass'

    natural_park_id = fields.Many2one('ges.natural_park', string="Natural Park", ondelete='cascade', required=True)

    name = fields.Char(string="Nombre", required=True)
    extension = fields.Integer(string="Extensión", required=True)
    areas_species_ids = fields.One2many(
        'ges.areass_species', 'areas_id', string="Areas")

    @api.constrains('extension')
    def _check_park_has_extension(self):
        for r in self:
            if r.extension <= 0:
                raise exceptions.ValidationError("La extensión no puede ser 0")
  

class Areas_Species(models.Model):
    _name = 'ges.areas_species'

    areas_id = fields.Many2one('ges.areas',
        ondelete='set null', string="Area")
    species_id = fields.Many2one('ges.species',
        ondelete='set null', string="Especie")

    individual_in_area = fields.Integer(string="Individuos de las especie en el area", required=True)
from odoo import models, fields, api, exceptions

class areas(models.Model):
    _name = 'iracema.areas'

    name = fields.Char(string="Nombre", required=True)
    natural_park_id = fields.Many2one('iracema.natural_park', string="Natural Park", ondelete='cascade', required=True)
    extension = fields.Integer(string="Extensión", required=True)
    areas_species_ids = fields.One2many(
        'iracema.areas_species', 'areas_id', string="Areas")

    @api.constrains('extension')
    def _check_park_has_extension(self):
        for r in self:
            if r.extension <= 0:
                raise exceptions.ValidationError("The extension must be greater than zero")
  

class areas_Species(models.Model):
    _name = 'iracema.areas_species'

    areas_id = fields.Many2one('iracema.areas',
        ondelete='set null', string="Area")
    species_id = fields.Many2one('iracema.species',
        ondelete='set null', string="Especie")
    individual_in_area = fields.Integer(string="Indiviuals in an area", required=True)

    @api.constrains('individual_in_area')
    def is_positive(self):
        for r in self:
            if r.individual_in_area <= 0:
                raise exceptions.ValidationError("The number must be grater than zero")
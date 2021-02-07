from odoo import models, fields, api, exceptions

class Staff(models.Model):
    _name = 'appnaturalparks.staff'

    name = fields.Char(string="Name", required=True)
    dni = fields.Char(required=True)
    social_security = fields.Char(required=True)
    address = fields.Char()
    mobile_phone = fields.Char()
    home_phone = fields.Char()
    salary = fields.Integer(string="Salary (in €, annual)")

    natural_park_id = fields.Many2one('appnaturalparks.natural_park', ondelete='cascade', string="Natural Park", required=True)

    @api.constrains('salary')
    def _check_park_has_extension(self):
        for s in self:
            if s.salary <= 0:
                raise exceptions.ValidationError("The salary must be higher than zero")

    class Management(models.Model):
    _name = 'appnaturalparks.management'
    _inherit = 'apnaturalparks.staff'

    number_entrance = fields.Integer()

    class Vigilance(models.Model):
    _name = 'appnaturalparks.vigilance'
    _inherit = 'appnaturalparks.staff'

    area_id = fields.Many2one('appnaturalparks.area', string="Area", required=True)

    class Research(models.Model):
    _name = 'appnaturalparks.research'
    _inherit = 'appnaturalparks.staff'

    title = fields.Char(required=True)

    class Conservation(models.Model):
    _name = 'appnaturalparks.conservation'
    _inherit = 'appnaturalparks.staff'

    speciality = fields.Selection([('cleaning', 'Cleaning'), ('roads', 'Roads'), ('others', 'Others')])

    area_id = fields.Many2one('appnaturalparks.area', string="Area", required=True) 
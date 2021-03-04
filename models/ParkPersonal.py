from odoo import models, fields, api, exceptions

class Parkpersonal(models.Model):
    _name = 'naturalparks.parkpersonal'

    name = fields.Char(string="name of the employee", required=True)
    dni = fields.Char(string="dni of the employee", required=True)
    ss_number = fields.Char(string="social security number of the employee", required=True)
    natural_park_id = fields.Many2one('naturalparks.natural_park', ondelete='cascade', string="Natural Park", required=True)
    address = fields.Char(string="address of the employee")
    mobile_phone = fields.Char(string="mobile phone of the employee")
    home_phone = fields.Char(string="home phone of the employee")
    salary = fields.Integer(string="salary of the employee")

    @api.constrains('salary')
    def _check_park_has_extension(self):
        for r in self:
            if r.salary <= 0:
                raise exceptions.ValidationError("error")

class Managementper(models.Model):
    _name = 'naturalparks.managementper'
    _order = 'name'
    _inherit = 'naturalparks.parkpersonal'

    number_of_entry = fields.Integer()

class Surveillanceper(models.Model):
    _name = 'naturalparks.surveillanceper'
    _order = 'name'
    _inherit = 'naturalparks.parkpersonal'

    area_id = fields.Many2one('naturalparks.area', string="area", required=True)
    personalcar_id = fields.Many2one('naturalparks.personalcar', string="personalcar", required=True)

class Personalcar(models.Model):
    _name = 'naturalparks.personalcar'
    _order = 'name'

    name = fields.Char(string="car model", required=True)

class Researchper(models.Model):
    _name = 'naturalparks.researchper'
    _order = 'name'
    _inherit = 'naturalparks.parkpersonal'

    title = fields.Char(string="tittle of the employee", required=True)

class Conservationper(models.Model):
    _name = 'naturalparks.conservationper'
    _order = 'name'
    _inherit = 'naturalparks.parkpersonal'

    area_id = fields.Many2one('naturalparks.area', string="Area", required=True)
    specialty = fields.Selection([('cleaning', 'Cleaning'), ('roads', 'Roads'), ('others', 'Others')]) 

 
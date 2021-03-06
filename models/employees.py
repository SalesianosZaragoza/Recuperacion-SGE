from odoo import models, fields, api, exceptions

class employees(models.Model):
    _name = 'odooIracema.employees'
    
    name = fields.Char(string="Name", required=True) 
    dni = fields.Char(required=True)
    social_security_number = fields.Char(required=True)
    address = fields.Char(required=True)
    mobile_phone = fields.Char(required=True)
    landline_phone = fields.Char(required=True)
    salary = fields.Integer(required=True, string="Anual salary in euros")

    @api.constrains('salary')
    def is_positive(self):
        for r in self:
            if r.salary <= 0:
                raise exceptions.ValidationError("The salary must be greater than zero")

class management(models.Model):
    _name = 'odooIracema.management'
    _inherit = 'odooIracema.employees'

    entrance_id = fields.Many2one('odooIracema.entrances', string="Entrance", required=True)
    
class entrances(models.Model):
    _name = 'odooIracema.entrances'

    entrance_number = fields.Integer(required=True)

class vehicles(models.Model):
    _name = 'odooIracema.vehicles'

    name = fields.Char(string="Car Type", required=True)
    plate_number = fields.Char(string="Plate number")
    car_model = fields.Char(string="Car model")

class investigation(models.Model):
    _name = 'odooIracema.investigation'
    _inherit = 'odooIracema.employees'

    academic_qualification = fields.Char(string="Titulation", required=True)    

    
class conservation(models.Model):
    _name = 'odooIracema.conservation'
    _inherit = 'odooIracema.employees'

    areas_id = fields.Many2one('odooIracema.areas', string="Area", required=True)
    specialty = fields.Selection([('cleaning', 'Cleaning'), ('canine', 'Canine'), ('prune', 'Prune')]) 

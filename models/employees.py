from odoo import models, fields, api, exceptions

class employees(models.Model):
    _name = 'ges.employees'
    
    name = fields.Char(string="Name", required=True) 
    dni = fields.Char(required=True)
    social_security_number = fields.Char(required=True)
    address = fields.Char(required=True)
    mobile_phone = fields.Char(required=True)
    landline_phone_phone = fields.Char(required=True)
    salary = fields.Integer(required=True, string="Anual salary in euros")

    @api.constrains('salary')
    def is_positive(self):
        for r in self:
            if r.salary <= 0:
                raise exceptions.ValidationError("The salary must be positive")

class management(models.Model):
    _name = 'ges.management'
    _inherit = 'ges.employees'

    entrance_id = fields.Many2one('ges.entrances', string="Entrance", required=True)
    
class entrances(models.Model):
    _name = 'ges.entrances'

    entrance_number = fields.Integer(required=True)

class surveillance(models.Model):
    _name = 'ges.surveillance'
    _inherit = 'ges.employees'

    car_id = fields.Many2one('ges.vehicles', string="Car", required=True)

class vehicles(models.Model):
    _name = 'ges.vehicles'

    name = fields.Char(string="Car Type", required=True)
    plate_number = fields.Char(string="Plate number")
    car_model = fields.Char(string="Car model")

class investigation(models.Model):
    _name = 'ges.investigation'
    _inherit = 'ges.employees'

    academic_qualification = fields.Char(string="Titulation", required=True)
    
class project(models.Model):
    _name = 'ges.project'

    name = fields.Char(string="Project Name", required=True)
    investigation_ids = fields.Many2many('ges.investigation', string="Investigators", required=True)
    species_id = fields.Many2one('ges.species', string="Especies", required=True)
    budget = fields.Float(string="Budget (in €)", digits=(8, 2))
    starting_date = fields.Date(required=True)
    ending_date = fields.Date(required=True)
    color = fields.Integer()
    state = fields.Selection([
            ('1.draft', 'Draft'),
            ('2.confirm', 'Confirm'),
            ('3.done', 'Done'),
        ], string='Status', default='1.draft')

    @api.constrains('starting_date', 'ending_date')
    def _check_ending_date_is_after_starting_date(self):
        for r in self:
            if r.starting_date > r.ending_date:
                raise exceptions.ValidationError("The initial date has to be prior to the ending date")

    def action_confirm(self):
        for r in self:
            r.state = '2.confirm'
            
    def action_done(self):
        for r in self:
            r.state = '3.done'

    def action_draft(self):
        for r in self:
            r.state = '1.draft'

class Conservation(models.Model):
    _name = 'ges.conservation'
    _inherit = 'ges.employees'

    areas_id = fields.Many2one('ges.areas', string="Area", required=True)
    specialty = fields.Selection([('cleaning', 'Cleaning'), ('canine', 'Canine'), ('prune', 'Prune')]) 

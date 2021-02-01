from odoo import models, fields, api, exceptions

class Employees(models.Model):
    _name = 'ges.employees'
    
    name = fields.Char(string="Name", required=True) 
    dni = fields.Char(required=True)
    social_security_number = fields.Char(required=True)
    address = fields.Char(required=True)
    mobile_phone = fields.Char(required=True)
    landline_phone = fields.Char(required=True)
    salary = fields.Integer(required=True, string="Salario anual en euros")

class Management(models.Model):
    _name = 'ges.gestion'
    _inherit = 'ges.employees'

    entrance_id = fields.Many2one('ges.entrances', string="Entrance", required=True)
    
class Entrances(models.Model):
    _name = 'ges.entrances'

    entrance_number = fields.Integer(required=True)

class Surveillance(models.Model):
    _name = 'ges.surveillance'
    _inherit = 'ges.employees'

    car_id = fields.Many2one('ges.vehicles', string="Car", required=True)

class Vehicles(models.Model):
    _name = 'ges.vehicles'

    name = fields.Char(string="Car Type", required=True)
    plate_number = fields.Char(string="Plate number")
    car_model = fields.Char(string="Car model")

class Investigation(models.Model):
    _name = 'ges.investigation'
    _inherit = 'ges.employees'

    academic_qualification = fields.Char(string="Titulacion", required=True)
    project_investigation_ids = fields.One2many(
        'ges.project_investigation', 'investigation_id', string="Investigador")

class Project_Investigation(models.Model):
    _name = 'ges.project_investigation'
    _inherit = 'ges.employees'

    investigation_id = fields.Many2one('ges.investigation',
        ondelete='set null', string="Investigador")
    project_id = fields.Many2one('ges.project',
        ondelete='set null', string="Proyecto")

class Project(models.Model):
    _name = 'ges.project'

    project_investigation_ids = fields.One2many(
        'ges.project_investigation', 'project_id', string="Proyecto")
    species_id = fields.Many2one('ges.species', string="Especies", required=True)
    budget = fields.Float(string="Budget (in €)", digits=(8, 2))
    starting_date = fields.Date(required=True)
    ending_date = fields.Date(required=True)

    @api.constrains('starting_date', 'ending_date')
    def _check_ending_date_is_after_starting_date(self):
        for r in self:
            if r.starting_date > r.ending_date:
                raise exceptions.ValidationError("La fecha de final tiene que ser posterior a la de inicio")

    #Aqui se podria añadir el panel kanban

class Conservation(models.Model):
    _name = 'ges.conservation'
    _inherit = 'ges.employees'

    area_id = fields.Many2one('ges.area', string="Area", required=True)
    specialty = fields.Selection([('cleaning', 'Cleaning'), ('canine', 'Canine'), ('prune', 'Prune')]) 

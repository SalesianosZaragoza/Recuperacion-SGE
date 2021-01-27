from odoo import models, fields, api, exceptions

class Employees(models.Model):
    _name = 'ges.employees'

class Management(models.Model):
    _name = 'ges.gestion'
    _inherit = 'ges.employees'

class Entrances(models.Model):
    _name = 'ges.entrances'

class Surveillance(models.Model):
    _name = 'ges.surveillance'
    _inherit = 'ges.employees'

class Vehicles(models.Model):
    _name = 'ges.vehicles'

class Investigation(models.Model):
    _name = 'ges.investigation'

class Project(models.Model):
    _name = 'ges.project'

class Conservation(models.Model):
    _name = 'ges.conservation'
    _inherit = 'ges.employees'

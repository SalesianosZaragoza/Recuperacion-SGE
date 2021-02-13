from odoo import models, fields, api, exceptions

class accommodation(models.Model):
    _name = 'ges.accommodation'
    _order = 'name'

    name = fields.Char(string="Name", required=True)
    capacity = fields.Integer(required=True)
    category = fields.Selection([('one', '*'), ('two','**'), ('three', '***'), ('four', '****'), ('five', '*****')])
    natural_park_id = fields.Many2one('ges.natural_park', string="Natural Park", ondelete='cascade', required=True)

class visitor(models.Model):
    _name = 'ges.visitor'

    name = fields.Char(required=True)    
    dni = fields.Char(required=True)
    address = fields.Char(required=True)
    job = fields.Char(required=True)

class excursions(models.Model):
    _name = 'ges.excursions'

    name = fields.Char(string="Excursion", required=True)
    excursion_type = fields.Selection([('car', 'Car'), ('walking', 'Walking')]) 
    starting_date = fields.Datetime(required=True)
    ending_date = fields.Datetime(required=True)

    accommodation_id = fields.Many2one('ges.accommodation', string="accommodation Organizer", required=True)
    visitor_ids = fields.Many2many('ges.visitor', string="Visitors")


    

    
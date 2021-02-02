from odoo import models, fields, api, exceptions

class Accommodation(models.Model):
    _name = 'ges.Accommodation'

    capacity = fields.Integer(required=True)
    category = fields.Selection([('one', '*'), ('two','**'), ('three', '***'), ('four', '****'), ('five', '*****')])
    natural_park_id = fields.Many2one('ges.natural_park', string="Natural Park", ondelete='cascade', required=True)
    visitor_ids = fields.One2many(
        'ges.visitor', 'accomodation_id', string="Alojamiento")
    total_visitors = fields.Integer(compute='_calculate_visitors')

    @api.depends('visitor_ids')
    def _calculate_visitors(self):
        for r in self:
            r.total_visitors = len(r.visitor_ids)

    @api.constrains('capacity', 'total_visitors')
    def _overbooking(self):
        for r in self:
            if r.total_visitors > r.capacity:
                raise exceptions.ValidationError("El numero de alojados supera la capacidad maxima")   

class Visitor(models.Model):
    _name = 'ges.Visitor'

    name = fields.Char(required=True)    
    dni = fields.Char(required=True)
    address = fields.Char(required=True)
    job = fields.Char(required=True)

class Excursions(models.Model):
    _name = 'ges.Excursions'

    name = fields.Char(string="Escursion", required=True)
    excursion_type = fields.Selection([('car', 'Car'), ('walking', 'Walking')]) 
    starting_date = fields.Datetime(required=True)
    ending_date = fields.Datetime(required=True)

    acommodation_id = fields.Many2one('ges.acommodation', string="Acommodation Organizer", required=True)
    visitor_ids = fields.Many2many('ges.visitor', string="Visitors")
    #Con domain se puede controlar para que solo salgan los valores que se quieran
    #habria que sacar solo los visitantes que estan en un alojamiento del parque natural

    

    
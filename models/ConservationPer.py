from odoo import models, fields, 

class ConservationPer(models.Model):
    _name='NaturalParks.ConservationPer'
    _order='Name'
    _inherit='NaturalParks.ParkPersonal'


    Name = fields.Char(string="name of the employee")
    Specialty = fields.Selection([('cleaning', 'Cleaning'), ('roads', 'Roads'), ('others', 'Others')])
    

    AreaID = fields.Many2one('NaturalParks.Area')


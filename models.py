# -*- coding: utf-8 -*-
from odoo import models, fields, api, exceptions 
import time
from datetime import timedelta
from odoo import models, fields
from odoo.exceptions import ValidationError
from openerp.exceptions import ValidationError
import json
import random
import urllib.request
from string import digits
from dataclasses import fields
import string
from encodings.punycode import digits

class Community(models.Model):
    _name = 'manager.community'

    name= fields.Char(string="Name community", required=True)
    park_id = fields.One2many(
        'manager.park', 'community_id', string = "Park")
    
class Park(models.Model):
    _name = 'manager.park'

    name = fields.Char(string="Name Park", required=True)
    starting_date = fields.Date(required=True)
    community_park_id = fields.One2many(
        'manager.comunity_park', 'community_id', string="Park")
    area_id = fields.One2many(
        'manager.area', 'park_id', string = "Area")
    species_id = fields.One2many(
        'manager.species', 'park_id', string = "Species")
    staff_id = fields.Many2one('manager.staff', string="Staff")    

class Acommodation(models.Model):
    _name = 'manager.accommodation'

    name = fields.Char(string="Name accommodation", required=True)
    capacity = fields.Integer(digits=(9), required=True)
    category = fields.Selection([('one', '*'), ('two','**'), ('three', '***')])	 
    staff_management_id = fields.Many2one('manager.staff_management', string="Staff management")
    park_id = fields.Many2one('manager.park', string="Park")
    visitor_id = fields.One2many(
        'manager.visitor', 'accommodation_id', string="Visitor")

    excursion_area = fields.Char(string="Excursion area", required=False)
    excursion_form = fields.Selection([(('on_foot', 'On_foot'), ('by_car', 'SpringBy_car'))])
    start_date = fields.Date(
        string="Start Date", store=True, default=fields.Date.today)
    end_date = fields.Date(string="End Date", store=True)

    duration = fields.Float(
        digits=(6, 2), help="Duration in days", compute='_days_duration')

    @api.one
    def _days_duration(self):
        if (self.end_date and self.start_date):
            start = fields.Datetime.from_string(self.start_date)
            end = fields.Datetime.from_string(self.end_date)
            self.duration = (end - start).days + 1

    @api.onchange('start_date', 'end_date')
    def _days_changed(self):
        for days in self:
            if(days.start_date or days.end_date):
                start = fields.Datetime.from_string(self.start_date)
                end = fields.Datetime.from_string(self.end_date)
                self.duration = (end - start).days + 1
                return {
                    'warning': {
                        'title': "Duration",
                        'message': "The duration has been updated " ,
                    }
                
@api.constrains('capacity')
def _check_something(self):
    for record in self:
        if record.capacity < 20:
            raise ValidationError("Your record is too old: %s" % record.capacity)
    # all records passed the test, don't return anything
                }
              
   
class Visitor(models.Model):
    _name = 'manager.visitor'
    
    name = fields.Char(string="Name visitor", required=True)    
    dni = fields.Text(string="DNI", required=True)	    
    address = fields.Char(string="Adress", required=True)	    
    profession = fields.Char(string="Profession", required=True)	
    use_excursion = fields.Boolean(string="Use excursion")
    staff_management_id = fields.Many2one('manager.staff_management', string="Management")
    accommodation_id = fields.Many2one('manager.accommodation', string="Accommodation")    
     
    entry_date= fields.Date(
        string="entry_date", store=True, default=fields.Date.today)
    

class Area(models.Model):
    _name = 'manager.area'

    name= fields.Char(string="Area", required=True)
    extension = fields.Float(digits=(20,3), required=True)

    park_area_id = fields.One2many(
        'manager.park_area', 'area_id', string="Area")
    staff_survellance_id = fields.One2many(
        'manager.staff_survellance', 'area_id', string="Survellance")
    staff_conservation_id = fields.One2many(
        'manager.staff_conservation', 'area_id', string="Conservation")



class Species(models.Model):
    _name = 'manager.species'

    scientific_name = fields.Char(string="Scientific_name", required=True)
    vulgar_name = fields.Char(string="Vulgar_name", required=True)
    classify = fields.Selection([('plant', 'Plant'), ('animal','Animal'), ('mineral', 'Mineral')])
    park_id = fields.Many2one('manager.park', string="Park")
    _inherit = 'base.entidad'

class Plant_species(models.Model):
    name = 'manager.plant_species'
    _inherit = 'manager.species'

    name = fields.Char(string="Plant species", required=True)
    flowering = fields.Boolean(string="It is the flowering period?")
    flowering_period = fields.Selection([(('winter', 'Winter'), ('spring', 'Spring'), 
    ('summer', 'Summer'), ('autumn', 'Autumn'))])
    inventory = fields.float(intdigits=(10,3), required=True)
     

class Animal_species(models.Model):
    _name = 'manager.animal_species'
    _inherit = 'manager.species'

    name = fields.Char(string="Animal species", required=True)
    feeding_type = fields.Selection([(('herbivore', 'Herbivore'), 
        ('carnivorous', 'Carnivorous'), 
        ('omnivorous', 'Omnivorous'))])
    heat_period = fields.Selection([(('herbivore', 'Herbivore'), 
        ('carnivorous', 'Carnivorous'), 
        ('omnivorous', 'Omnivorous'))])
    inventory = fields.Char(int=(10,3), required=True)
   
class Mineral_species(models.Model):
    _name = 'manager.mineral_species'
    _inherit = 'manager.species'

    name = fields.Char(string="Mineral species", required=True)
    category = fields.Selection([(('crystal', 'Cristal'), 
      ('stone', 'Stone'))])
    inventory = fields.Char(int=(10,3), required=True)


class Staff(models.Model):
    _name = 'manager.staff'

    name = fields.Char(string="Staff", required=True)
    DNI = fields.Char(string="DNI", required=True)
    social_security= fields.Char(string="Social security", required=True)
    adress= fields.Char(string="Adress", required=True)
    mobile= fields.Integer(int=(9), required=True)
    salary= fields.Float(float="Salary", required=True)
    type= fields.Selection(
        [(('managment', 'Managment'), ('survellance', 'Survellance'), 
        ('research', 'Research'), ('conservation', 'Conservation'))])
    park_id = fields.One2many('manager.park', 'staff_id', string="Park")
    _inherit = 'base.entidad'

class Staff_management(models.Model):
    _name = 'manager.staff_management'
    _inherit = 'manager.staff'

    name = fields.Char(string="Management", required=True)
    entry= fields.Integer(int=(10), required=True)

class Staff_survellance(models.Model):
    _name = 'manager.staff_survellance'
    _inherit = 'manager.staff'

    name = fields.Char(string="Survellance", required=True)
    car_type= fields.Char(string="Car type", required=True)
    enrollment= fields.Integer(int="Enrollment", required=True)
    area_id = fields.Many2one('manager.area', string="Area")

class Staff_research(models.Model):
    _name = 'manager.staff_research'
    _inherit = 'manager.staff'
    
    name = fields.Char(string="Research", required=True)
    title= fields.Char(string="Title", required=True)
    project_id = fields.Many2one('manager.project', string="Project")

class Staff_conservation(models.Model):
    _name = 'manager.staff_conservation'
    _inherit = 'manager.staff'

    name = fields.Char(string="Conservation", required=True)
    specialization= fields.Char(string="Specialization", required=True)


class Project(models.Model):
_name = 'manager.project'
   

    name = fields.Char(string="Project", required=True)
    project_about = fields.Char(string="Project about", required=True)
    budget = fields.Float(float="Budget", required=True)
    staff_research_id = fields.One2many(
        'manager.staff_research', 'project_id', string="Project")
    start_date = fields.Date(
        string="Start Date", store=True, default=fields.Date.today)
    end_date = fields.Date(string="End Date", store=True)

    period = fields.Float(
        digits=(6, 2), help="Period in days", compute='_days_duration')

    

    @api.one('period')
    def _days_period(self):
        if (self.end_date and self.start_date):
            start = fields.Datetime.from_string(self.start_date)
            end = fields.Datetime.from_string(self.end_date)
            self.duration = (end - start).days + 1

    @api.onchange('start_date', 'end_date')
    def _days_changed(self):
        for days in self:
            if(days.start_date or days.end_date):
                start = fields.Datetime.from_string(self.start_date)
                end = fields.Datetime.from_string(self.end_date)
                self.duration = (end - start).days + 1
                return {
                    'warning': {
                        'title': "Period",
                        'message': "The period has been updated",
                     },
                }

© 2021 Manager Natural Parks, Inc
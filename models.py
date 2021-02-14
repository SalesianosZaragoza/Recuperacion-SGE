# -*- coding: utf-8 -*-
from odoo import models, fields, api


class Community(models.Model):
    _name = 'manager.community'

    name= fields.Char(string="Name community", required=True)
    community_park_id = fields.One2many(
        'manager.community_park', 'community_id', string="Community parks")

    class Community_Park(models.Model):
     _name = 'manager.community_park'
    
    community_id = fields.Many2one(',manager.community',
        ondelete='set null', string="Community")
    park_id = fields.Many2one('manager.park',
        ondelete='set null', string="Park")

    class Park(models.Model):
     _name = 'manager.park'

    name = fields.Char(string="Name Park", required=True)
    starting_date = fields.Date(required=True)
    community_park_id = fields.One2many(
        'manager.community_park', 'community_id', string="Park") 
      
   
    class Visitor(models.Model):
     _name = 'manager.visitor'
    
    name= fields.Char(string="Name visitor", required=True)
    DNI = fields.Char(string="DNI", required=True)
	adress = fields.Char(string="Adress", required=True)
    profession = fields.Char(string="Profession", required=False)
    accommodation = fields.Char(string="Accommodation visitor", required=True)
    entry_date= fields.Date(
        string="entry_date", store=True, default=fields.Date.today)
     park_visitor_id = fields.One2many(
        'manager.park_visitor', 'park_id', string="Park visitors")

class Park_visitor(models.Model):
    _name = 'manager.park_visitor'
    
    name= fields.Char(string="Park visitors", required=True)
    park_id = fields.Many2one(',manager.park',
        ondelete='set null', string="Park")
    visitor_id = fields.Many2one('manager.visitor',
        ondelete='set null', string="Visitor")

    	
 class Species(models.Model):
	 _name = 'manager.species'
    
 	name = fields.Char(string="Scientific_name", required=True)
	name = fields.Char(string="Vulgar_name", required=True)
    type = fields.Char(string="Type", required=True)
    park_species_id = fields.One2many(
        'manager.park_species', 'species_id', string="Park species")
     
    
class Park_species(models.Model):
    _name = 'manager.park_species'
    
    name= fields.Char(string="Park species", required=True)
    park_id = fields.Many2one(',manager.park',
        ondelete='set null', string="Park")
    species_id = fields.Many2one('manager.species',
        ondelete='set null', string="Species")

class Area(models.Model):
  _name = 'manager.area'

    name= fields.Char(string="Area", required=True)
    area_species_id = fields.One2many(
        'manager.area_species', 'species_id', string="Area speciess")
   extension = fields.Integer(int=(20,3), required=True)

    class Area_species(models.Model):
     _name = 'manager.area_species'
    
    name= fields.Char(string="Area species", required=True)
    area_id = fields.Many2one(',manager.area',
        ondelete='set null', string="Area")
    species_id = fields.Many2one('manager.species',
        ondelete='set null', string="Species")   

	class Plant_species(models.Model):
	 _name = 'manager.plant_species'
     _inherit = 'manager.species'

    name = fields.Char(string="Plant species", required=True)
    flowering = fields.Boolean(string="It is the flowering period?")
    flowering_period = fields.Selection([(('winter', 'Winter'), ('spring', 'Spring'), 
    ('summer', 'Summer'), ('autumn', 'Autumn'))])
    inventory = fields.Char(int=(10,3), required=True)
     

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
    type= fields.Selection([(('managment', 'Managment'), 
     ('survellance', 'Survellance'), 
     ('research', 'Research'), ('conservation', 'Conservation'))])

     class Staff_management(models.Model):
    _name = 'manager.staff_management'
    _inherit = 'manager.staff'

	name = fields.Char(string="Name staff", required=True)
    entrada= fields.Integer(int=(10), required=True)

     class Staff_survellance(models.Model):
    _name = 'manager.staff_survellance'
    _inherit = 'manager.staff'

   name = fields.Char(string="Name", required=True)
   enrollment= fields.Integer(int="Enrollment", required=True)
   car_type= fields.Char(string="Car type", required=True)
   area= fields.Char(string="Area", required=True)

class Staff_research(models.Model):
    _name = 'manager.staff_research'
    _inherit = 'manager.staff'
    name = fields.Char(string="Name", required=True)
    project_id = fields.Char(string="Name project", required=True)
    area= fields.Char(string="Area", required=True)

  
class Project(models.Model):
    _name = 'manager.project'
    _inherit = 'manager.staff_research'

    project_about = fields.Char(string="Project about", required=True)
    budget = fields.Float(float="Budget", required=True)
    period = fields.Float(
        digits=(6, 2), help="Period in days", compute='_days_duration')

         @api.one
    def _days_period(self):
        if (self.end_date and self.start_date):
            start = fields.Datetime.from_string(self.start_date)
            end = fields.Datetime.from_string(self.end_date)
            self.period = (end - start).days + 1

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
                    }

                    
class Staff_conservation(models.Model):
    _name = 'manager.staff_conservation'
    _inherit = 'manager.staff'

    name = fields.Char(string="Name", required=True)
    specialization= fields.Char(string="Specialization", required=True)


     
class Accommodation(models.Model):
    _name = 'manager.accommodation'
     
	name = fields.Char(string="Name accommodation", required=True)
    excursion = fields.Char(string="Name excursion", required=False)
   
    excursion_form = fields.Selection(string="Name accommodation", required=True)
    community_park_id = fields.One2many(
        'manager.accommodation_visitor', 'accommodation_id', string="Accommodation visitors")

  
class Accommodation_visitor(models.Model):
  _name = 'manager.accommodation_visitor'
    
    accommodation_id = fields.Many2one(',manager.accommodation',
        ondelete='set null', string="Accommodation")
    visitor_id = fields.Many2one('manager.visitor',
        ondelete='set null', string="Visitor")
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
                        'message': "The duration has been updated",
                    }
                
# -*- coding: utf-8 -*-
from odoo import models, fields, api, exceptions 
import time
from datetime import timedelta
from odoo import models, fields
from odoo.exceptions import ValidationError
import json
import random
import urllib.request

class Community(models.Model):
    _name = 'recup.community'
    
    name = fields.Char(string="Nombre comunidad autonoma", required=True)
    organism = fields.Char(string="nombre organismo")
    park_id = fields.Many2many(
        'recup.park', 'community_park', 'community_id', 'park_id', 'park')
    
class Park(models.Model):
    _name = 'recup.park'
    
    name = fields.Char(string="Nombre Parque", required=True)
    creationYear = fields.Date(
        string="Start Date", store=True, default=fields.Date.today)
    community_id = fields.Many2many(
        'recup.community', 'community_park', 'park_id', 'community_id', 'community')
    area_id = fields.One2many('recup.area', 'park_id', string="area")
    accommodation_id = fields.One2many('recup.accommodation', 'park_id', string="accommodation")
    excursion_id = fields.One2many('recup.excursion', 'park_id', string="excursion")
    entries_id = fields.One2many('recup.entries', 'park_id', string="entries")


class Area(models.Model):
    _name = 'recup.area'
    
    name = fields.Char(string="nombre Area", required=True)
    extension = fields.Integer(string="extension") 
    park_id = fields.Many2one('recup.park', string="parks")
    species_id = fields.Many2many(
        'recup.species', 'area_species', 'area_id', 'species_id', 'species')
    vigilance_id = fields.One2many('recup.vigilance', 'area_id', string="vigilances")
    conservation_id = fields.One2many('recup.conservation', 'area_id', string="conservations")
    
    @api.constrains('extension')
    def _check_park_extension(self):
        for r in self:
            if r.extension <= 0:
                raise exceptions.ValidationError("The area must have extension")
    
class Species(models.Model):
    _name = 'recup.species'
    

    type_specie = fields.Selection(selection=[(
        '1', 'animal'), ('2', 'vegetal'), ('3', 'mineral')], string="tipo especie", default="1")
    scientific_name = fields.Char(String = "nombre cietifico")
    vulgar_name = fields.Char(String = "nombre vulgar")
    number_individuals = fields.Integer(string="numero de individuos")
    area_id = fields.Many2many(
        'recup.area', 'area_species', 'species_id', 'area_id', 'area')
    proyect_id = fields.Many2many('recup.proyect', 'proyect_species', 'species_id', 'proyect_id', 'proyect')
    
class Plant(models.Model):
    _name = 'recup.plant'
    _inherit = 'recup.species'
        

    blooming = fields.Boolean(string="¿tiene floracion?")
    blooming_period = fields.Selection([('spring', 'Spring'), ('summer', 'Summer'), ('autumn', 'Autumn'), ('winter', 'Winter')])

    is_eaten = fields.Boolean(string="Is this plant eaten?")
    animal_ids = fields.Many2many('recup.animal', string="Herbivoros que comen esta planta", 
        domain=[('alimentation', '!=', 'carnivore')])

        

class Animal(models.Model):
    _name = 'recup.animal'
    _inherit = 'recup.species'
        

    alimentation = fields.Selection([('carnivore','Carnivore'), ('herbivore','Herbivore'), ('omnivore','Omnivore')], required=True)
    mating_season = fields.Selection([('spring', 'Spring'), ('summer', 'Summer'), ('autumn', 'Autumn'), ('winter', 'Winter')])
    color = fields.Integer()

    is_eaten = fields.Boolean(string="Is this animal eaten?")
    plant_id = fields.Many2many(comodel_name='recup.animal', relation='animals_eaten', column1='prey', column2='carnivores', string="Carnivores which eat this animal",
        domain=[('alimentation', '!=', 'herbivore')])

        
class Mineral(models.Model):
    _name = 'recup.mineral'
    _inherit = 'recup.species'
        

    mineral_type = fields.Selection([('crystal', 'Crystal'), ('stone', 'Stone')], required=True)
    color = fields.Integer() 
        
class Personal(models.Model):
    _name = 'recup.personal'
    

    name = fields.Char(string="Nombre personal", required=True)
    dni = fields.Text(string="dni")
    numberSocialSecurity = fields.Text(string="num seguridad social")
    address = fields.Char(string="direccion")        
    phone = fields.Integer(string="telefono")
    salary = fields.Integer(string="sueldo")
    
class Management(models.Model):
    _name = 'recup.management'
    _inherit = 'recup.personal'
    registroVisitante = fields.Text(string="dni")
        
class Vigilance(models.Model):
    _name = 'recup.vigilance'
    _inherit = 'recup.personal'
    area_id = fields.Many2one('recup.vigilance', string="areas")
        
class Investigator(models.Model):
    _name = 'recup.investigator'
    _inherit = 'recup.personal'
    titulation = fields.Char(string="titulacion") 
    proyect_id = fields.Many2many('recup.proyect', 'proyect_investigator', 'investigator_id', 'proyect_id', 'proyect')  
class Conservation(models.Model):
    _name = 'recup.conservation'
    _inherit = 'recup.personal'
    speciality = fields.Char(string="especialidad")    
    area_id = fields.Many2one('recup.conservation', string="areas")
class Visitor(models.Model):
    _name = 'recup.visitor'
    

    name = fields.Char(string="nombre visitante", required="true")
    address = fields.Char(string="direccion")
    dni = fields.Text(string="dni")
    profession = fields.Char(string ="profesion")
    accommodation_id = fields.Many2one('recup.accommodation', string="accommodation" )
    excursion_id = fields.Many2many('recup.excursion', 'excursion_visitor', 'visitor_id', 'excursion_id', 'excursions')
    
    _sql_constraints = [       

     ('dni_unique',        

    'UNIQUE(dni)',        

    "The dni must be unique"),   

    ]

class Accommodation(models.Model):
    _name = 'recup.accommodation'
    

    name = fields.Char(string="Nombre alojamiento", required=True)
    capacity = fields.Integer(string="capacidad")
    category = fields.Char(string="categoria")
    park_id = fields.Many2one('recup.park', string="park")
    visitor_id = fields.One2many('recup.visitor', 'accommodation_id', string="visitors")
    @api.constrains('park_id', 'name')
    def _check_name_not_in_park(self):
        for r in self:
            if r.park_id and r.park_id in r.name:
                raise exceptions.ValidationError(
                    "A session's instructor can't be an attendee")
                
class Excursion(models.Model):
    _name = 'recup.excursion'
    

    name = fields.Char(string="Nombre excursion", required=True)
    
    active = fields.Boolean(default=True)
    color = fields.Integer()
    day = fields.Date(
        string="dia excursion", store=True, default=fields.Date.today)
    park_id = fields.Many2one('recup.park', string="parque")
    visitor_id = fields.Many2many('recup.visitor', 'excursion_visitor', 'excursion_id', 'visitor_id', 'visitors')
    mode_transport  = fields.Selection([
                    ('1', 'a pie'),
                    ('2', 'en coche')],
                    'modo de transporte', size=1
    
                     )   

class Entries(models.Model):
    _name = 'recup.entries'
    name = fields.Integer(string = "numero de entrada al parque")
    park_id = fields.Many2one('recup.park', string="park")

class Proyect(models.Model):
    _name = 'recup.proyect'
    species_id = fields.Many2many(
        'recup.species', 'proyect_species', 'proyect_id', 'species_id', 'species')
    investigator_id = fields.Many2many(
        'recup.investigator', 'proyect_investigator', 'proyect_id', 'investigator_id', 'investigators')
    budget = fields.Integer(string = "budget proyecto")
    start_date = fields.Date(
        string="Start Date", store=True, default=fields.Date.today)
    end_date = fields.Date(string="End Date", store=True)

    duration = fields.Float(
        digits=(6, 2), help="Duration in days", compute='_days_duration')
    state = fields.Selection([
            ('1.draft', 'Draft'),
            ('2.confirm', 'Confirm'),
            ('3.done', 'Done'),
        ], string='Status', default='1.draft')

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
                        'message': "La duracion ha sido actualizada",
                    },
                }
    
    def action_confirm(self):
        for r in self:
            r.state = '2.confirm'
            return {
                'effect': {
                    'fadeout': 'slow',
                    'message': 'Trip Confirmed',
                    'type': 'rainbow_man',
                }
            }

    def action_done(self):
        for r in self:
            r.state = '3.done'

    def action_draft(self):
        for r in self:
            r.state = '1.draft' 

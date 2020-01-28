# -*- coding: utf-8 -*-
from datetime import timedelta
from odoo import fields, models, api, exceptions
from odoo.exceptions import ValidationError



class Sith(models.Model):
    _name = 'war.sith'
    name = fields.Char(string="Sith")
    race = fields.Char(string="Race")
    rage = fields.Integer(string="Rage")
    darkAffinity = fields.Integer(string="Dark Affinity", compute='_get_darkAffinity')
    n_sabers = fields.Boolean(string="Double Saber")
    saber_color = fields.Selection([('r', 'Red'), ('d', 'Dark red')])
    jedis_id = fields.One2many('war.jedis', 'sith_id', string="Specie")
    
    @api.onchange('rage')
    def _get_darkAffinity(self):
        for r in self:
            r.darkAffinity = r.rage * 2 



class Jedis(models.Model):
    _name = 'war.jedis'
    name = fields.Char(string="Jedi")
    saber_color = fields.Selection([('b', 'Blue'), ('g', 'Green')])
    sith_id = fields.Many2one('war.sith', ondelete='cascade', string="Sith", required=True)
    last_date = fields.Date(string="Last record")
    planet_id = fields.Many2one('war.planet', ondelete='cascade', string="Planet", required=True)
    midiclorians = fields.Integer(string="Midiclorians")
    jedi_level = fields.Char(string="Jedi level", compute='_get_jedi_level')

    @api.depends('midiclorians')
    def _get_jedi_level(self):
        for r in self:
            if r.midiclorians < 100:
                r.jedi_level = "Padawan"
            elif r.midiclorians >= 100 and r.midiclorians < 1000:
                r.jedi_level = "Jedi Knight"
            else:
                r.jedi_level = "Advisor"
    
    @api.multi
    def copy(self, default=None):
        default = dict(default or {})

        copied_count = self.search_count(
            [('name', '=like', u"Copia de {}%".format(self.name))])
        if not copied_count:
            new_name = u"Copia de {}".format(self.name)
        else:
            new_name = u"Copia de {} ({})".format(self.name, copied_count)

        default['name'] = new_name
        return super(Jedis, self).copy(default)


    _sql_constraints = [
        ('name_unique',
         'UNIQUE(name)',
         "This jedi already exists."),
    ]

    @api.constrains('midiclorians')
    def _check_something(self):
        for record in self:
            if record.midiclorians > 100:
                   raise ValidationError("A very high level of midiclorians has been detected: %s" % record.midiclorians)



class Planet(models.Model):
    _name = 'war.planet'
    _description = 'Planets list'
    name = fields.Char(string="Planet")
    destroyed = fields.Boolean(string="Destroyed")
    date_des = fields.Date(string="Destruction date")
    distance = fields.Integer(string="Parsecs")
    specie_id = fields.One2many('war.specie', 'planet_id', string="Specie", required=True , compute='_kill_people')

    @api.depends('destroyed')
    def _kill_people(self):
        for r in self:
            print(r.destroyed)
            if r.destroyed == True:
                r.specie_id.unlink()          



class Specie(models.Model):
    _name = 'war.specie'
    _description = 'Species list'
    name = fields.Text(string="Specie")
    planet_id = fields.Many2one('war.planet',ondelete='cascade', string="Planet", required=True)
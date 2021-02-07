from odoo import models, fields

class especies(models.Model):
    _name = 'np.especies'

    nombre = fields.Char(string="", required=True)
    area.id = fields.Many2many('np.area', string="Area", required=True)
    nEspecies = fields.Integer()

class planta(models.Model):
    _name = 'np.planta'
    _inherit = 'np.especies'


    floracion = fields.Boolean(string="Tiene?")
    pFloracion = fields.Selection([('Otoño', 'Otoño'), ('Invierno', 'Invierno'), ('Primavera', 'Primavera'), ('Verano', 'Verano')])
    comestible = fields.Boolean(string="Es comestible")
    animal.id = fields.Many2many('np.animal', string="Depredadores", 
        domain=[('alimentation', '!=', 'carnivora')])

class animal(models.Model):
    _name = 'np.animal'
    _inherit = 'np.especies'


    alimentacion = fields.Selection([('carnivora','carnivora'), ('herbivora','herbivora'), ('omnivora','omnivora')], required=True)
    tApareamiento = fields.Selection([('Otoño', 'Otoño'), ('Invierno', 'Invierno'), ('Primavera', 'Primavera'), ('Verano', 'Verano')])
    color = fields.Integer()

    comestible = fields.Boolean(string="Comestible")
    animal.id = fields.Many2many(comodel_name='np.animal', relation='animales', column1='presa', column2='carnivoras', string="depredadores",
        domain=[('alimentation', '!=', 'herbivora')])

class mineral(models.Model):
    _name = 'np.mineral'
    _inherit = 'np.especies'


    tMineral = fields.Selection([('cristal', 'cristal'), ('piedra', 'piedra')], required=True)
    color = fields.Integer()
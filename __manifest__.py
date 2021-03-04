# -*- coding: utf-8 -*-
{
    'name': "Natural park information",

    'summary': """Park manager""",
    
    'description': """Module to manage parks in community:""",


    'author': "Iracema Sebastian",
    'website': "http://www.manager.park",

    # Categories can be used to filter modules in modules listing
    # for the full list
    'category': 'test',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'views/manager.xml',
        'views/community.xml',
        'views/park.xml',
        'views/accommodation.xml',
        'views/visitor.xml',
        'views/area.xml',
        'views/species.xml',
        'views/plant_species.xml',
        'views/animal_species.xml',
        'views/mineral_species.xml',
        'views/staff.xml',
        'views/management_staff.xml',
        'views/survellance_staff.xml',
        'views/research_staff.xml',
        'views/conservation_staff.xml',
        'views/project.xml',
        'security/ir.model.access.csv'
         ],

'installable': True,
   
}

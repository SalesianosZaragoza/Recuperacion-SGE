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
    'depends': ['base', 'board'],

    # always loaded
    'data': [
        'views/manager.xml',
        'security/ir.model.access.csv'
         ],

'installable': True,
   
}

# -*- coding: utf-8 -*-
{
    'name': "RecuperacionOdoo",

    'summary': """ Lee el readme.md  """
    'description': """
       Module to recovery Odoo
    """,


    'author': "Alberto Luna Lopez",
    'website': " ",

    # Categories can be used to filter modules in modules listing
    # for the full list
    'category': 'test',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'baseModule'],

    # always loaded
    'data': [
        'libraryWriter.xml',
        'security/ir.model.access.csv',
        'reporting.xml'
    ],  
}

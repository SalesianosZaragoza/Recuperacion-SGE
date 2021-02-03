
   # -- coding: utf-8 --
{
    'name': "App Natural Parks",

    'summary': """Una aplicación de parques naturales""",

    'description': """
        Una aplicación sobre los parques naturales de España
                - visitantes 
                - staff de los parques 
                - acomodacion
    """,

    'author': "Jorge Gimeno",
    'website': "",

    # Categories can be used to filter modules in modules listing
    # for the full list
    'category': 'Test',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'board'],

    # always loaded
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
       
        
    ],
} 
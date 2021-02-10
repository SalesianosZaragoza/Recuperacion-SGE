
   # -- coding: utf-8 --
{
    'name': "App Natural Parks",

    'summary': """Una aplicación de parques naturales""",

    'description': """
        Una aplicación sobre los parques naturales de España
                - visitantes 
                - staff de los parques 
                - hotel de alojamiento
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
        'views/area.xml',
        'views/community.xml',
        'views/excursion.xml',
        'views/hotel.xml',
        'views/naturalpark.xml',
        'views/species.xml',        
        'views/staff.xml',
        'views/visitor.xml',
        'reports/report_excursion.xml',
        'reports/report_visitor.xml',
    ],
} 
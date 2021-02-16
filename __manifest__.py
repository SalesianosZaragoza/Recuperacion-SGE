# -*- coding: utf-8 -*-
{
    'name': "recuperacion",

    'summary': """gorka always win""",
    
    'description': """
        este modulo contiene:
            -filtros de busqueda
            -calendario
            -model constraint
            -reporting en pdf
            -servicio rest con json
            -botones
            -kanban
    """,


    'author': "sergio roche almarcegui",
    'email': "seroal999@gmail.com",

    # Categories can be used to filter modules in modules listing
    # for the full list
    'category': 'test',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'board'],

    # always loaded
    'data': [
        'recup.xml',
        'security/ir.model.access.csv',
        'report.xml',
    ],

  

}
# -*- coding: utf-8 -*-
{
    'name': "Módulo de Autores y Libros",

    'summary': """Módulo para recuperar Odoo""",

    'description': """
        Este módulo contiene:
            - relaciones muchos a muchos
            - filtro de búsqueda
            - vista de calendario
            - model constraint implementado
            - sistema de reporting
            - servicio de api rest
            - vista de kanban
    """,

    'author': "Mateo Bernal Tejeda",
    'email': "mbertej2000@gmail.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Test',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'baseModule'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'vista.xml','reports.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo.xml',
    ],
}

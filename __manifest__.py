# -*- coding: utf-8 -*-
{
    'name': "AutorLibros",

    'summary': """Modulo de la recuperacion""",

    'description': """
        MOdulo fabricado para pruebas con Odoo 12 para el examen sobre AutorLibros
    """,

    'author': "Ismael Valero",
    'website': "http://www.ismaelvalero.pt",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Test',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','baseModule'],

    # always loaded
    'data': [
        'views/views.xml',
        'views/reporting.xml',
        'Api_Rest/QwebJson.json'
    ],
    # only loaded in demonstration mode
    #'demo': [
     #   'demo.xml',
    #],
}

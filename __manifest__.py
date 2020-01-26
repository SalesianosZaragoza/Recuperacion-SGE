# -*- coding: utf-8 -*-
{
    'name': "Libros y Autores",

    'summary': """
        Recuperación""",

    'description': """
        Recuperación de Odoo en la que se usan ejemplos de libros y autores
    """,

    'author': "Jefferson Chanchicocha",
    'website': "https://zaragoza.salesianos.edu/",
    'category': 'Odoo',
    'version': '1.0',
    'depends': ['base'],
    'data': [
        'views/base.xml',
        'reports/report.xml',
        'reports/book.xml',
    ],
}
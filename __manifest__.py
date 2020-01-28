# -*- coding: utf-8 -*-
{
    'name': "Open Academy",

    'summary': """Odoo library project""",

    'description': """
        Includes everything necessary to get this PR accepted (I hope)
    """,

    'author': "Lolmatyc TM",
    'website': "http://www.reddit.com/r/lolmatyc",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Recu',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'baseModule'],

    # always loaded
    'data': [
        'views/view.xml',
        'views/calendar.xml',
        'views/reports.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo.xml',
    ],
}

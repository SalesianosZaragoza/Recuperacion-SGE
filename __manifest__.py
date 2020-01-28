# -*- coding: utf-8 -*-
{
    'name': "Remedial exam Odoo",

    'summary': """Hoping for the best""",

    'description': """
        Remedial exam module with the purpose of making our professor feel better about his students
    """,

    'author': "Valero Mateo",
    'website': "http://www.mybigassdisaster.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Test',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'baseModule'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'openacademy.xml',
        'reports.xml'
    ],
   
}

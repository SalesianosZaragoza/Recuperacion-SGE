{
    'name': "NPI",

    'summary': """Natural Parks Information""",

    'description': """
        Natural Park module for giving information:
            - routes
            - clients
            - fauna
    """,

    'author': "Javier Gumiel",
    'website': "http://www.yourcompany.com",

    'category': 'Test',
    'version': '0.1',

    'depends': ['base'],

    'data': [
        'views/area.xml',
        'views/ca.xml',
        'views/naturalPark.xml',
        'views/project.xml',
        'views/route.xml',
        'views/species.xml',
        'views/staff.xml',
        'views/visitor.xml',
    ],
}

{
    'name': "Natural Park",

    'summary': """Manage Natural Parks""",

    'description': """
        Manage Natural Parks module for get a five:
            - training courses
            - training sessions
            - attendees registration
    """,

    'author': "Gabriel Burgos",
    'website': "http://www.yourcompany.com",

    'category': 'Test',
    'version': '0.1',

    'depends': ['base','baseModule'],
    
    'data': [
        'views/naturalPark.xml',
        'views/acommodation.xml',
        'views/area.xml',
        'views/community.xml',
        'views/project.xml',
        'views/species.xml',
        'views/staff.xml',
        'views/travel.xml',
        'views/travellers.xml',
    ],
   
}
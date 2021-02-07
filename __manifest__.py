
{
    'name': "recuperacionOdoo",

    'summary': """modulo de recuperacion""",

    'description': """
        modulo recuperacion
    """,

    'author': "Marcos Garcés",
    'website': "http://www.yourcompany.com",
    'category': 'Test',
    'version': '0.1',
    'depends': ['base', 'board'],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/accommodation/accommodation.xml',
        'views/accommodation/visitor.xml',
        'views/accommodation/excursions.xml',
        'views/areas/areas.xml',
        'views/areas/areas_species.xml',
        'views/autonomous_community/autonomous_community_natural_park.xml',
        'views/autonomous_community/autonomous_community.xml',
        'views/employees/consevation.xml',
        'views/employees/entrances.xml',
        'views/employees/management.xml',
        'views/employees/natural_park.xml',
        'views/employees/project.xml',
        'views/employees/surveillance.xml',
        'views/employees/vehicles.xml',
        'views/natural_park/natural_park.xml',
        'views/species/vegetable.xml',
        'views/species/animal.xml',
        'views/species/mineral.xml',
        'reports/report_animal.xml',
        'reports/report_mineral.xml',
        'reports/report_vegetable.xml',
        'reports/report_natural_park.xml'
    ],

}
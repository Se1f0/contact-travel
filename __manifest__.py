{
    'name': "Contact Travel",
    'summary': "Module personnalisé de gestion des contacts liés aux voyages",
    'description': "Ce module vous permet de gérer les contacts liés aux voyages avec un système automatique de niveau de récompense.",
    'author': "Seif Eddine Segueni",
    'category': 'Uncategorized',
    'version': '0.1',
    'depends': ['base'],
    'data': [
        'security\ir.model.access.csv',
        'views\menu.xml',
        'views\\voyage_views.xml',
        'views\\res_partner_views.xml',
    ],
    'installable': True,
    'application': True,
    'sequence': -100,
}

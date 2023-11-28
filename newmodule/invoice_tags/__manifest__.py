# -*- coding: utf-8 -*-

{
    'name': 'Invoice Tags',
    'version': '16.0.1.0.0',
    'category': 'Invoice',
    'summary': 'Invoice Management',
    'description': "invoice tags management",
    'author': 'Abhilash',
    'website': 'https://www.yourwebsite.com',
    'depends': ['base', 'account'],
    'data': [
        'views/invoice_tags_views.xml',
        'security/ir.model.access.csv',
        'views/invoice_form_tags_views.xml',
        'views/invoice_tree_tags_views.xml',
        'views/invoice_menu.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}

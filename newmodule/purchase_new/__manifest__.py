# -*- coding: utf-8 -*-

{
    'name': 'Purchase New',
    'author': 'abhilash',
    'version': '16.0.1.0.0',
    'category': 'Technical_side',
    'depends': ['base','purchase','sale','project'],
    'description': "Purchase",
    'data': ['views/purchase_new_views.xml',
             'views/purchase_inherit_views.xml',
             'views/project_inherit_code.xml',
             'views/sale_inherit_views.xml',
             'security/mrp_access.xml',
             'data/product_code.xml',
             'data/project_code.xml',
             'report/purchase_print.xml'],
    'installable': True,
    'auto_install': False,
    'application': True,
}


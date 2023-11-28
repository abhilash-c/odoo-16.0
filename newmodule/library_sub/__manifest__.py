# -*- coding: utf-8 -*-
{
    'name': 'library sub',
    'author': 'abhilash',
    'version': '16.0.1.0.0',
    'category': 'Book',
    'depends': ['base', 'library'],
    'description': "A collection or group of collections of books and/or other print or nonprint materials organized "
                   "and maintained for use reading, consultation, study, research, etc.",
    'data': ['views/inherit_library_views.xml',
             'views/inherit_category_views.xml',],
    'installable': True,
    'auto_install': False,
    'application': True,
}

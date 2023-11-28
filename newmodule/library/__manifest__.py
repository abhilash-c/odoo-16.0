# -*- coding: utf-8 -*-
{
    'name': 'library',
    'author': 'abhilash',
    'version': '16.0.1.0.0',
    'category': 'Book',
    'depends': ['base'],
    'description': "A collection or group of collections of books and/or other print or nonprint materials organized "
                   "and maintained for use reading, consultation, study, research, etc.",
    'data': [
             'security/ir.model.access.csv',
             'security/library_access.xml',
             'security/library_security.xml',
             'views/library_views.xml',
             'views/library_menus.xml',
             'views/library_book_publisher_views.xml',
             'views/library_book_category_views.xml',
             'views/library_book_rent_views.xml',
             'wizard/return_book_views.xml',
             'wizard/rent_book_wizard_views.xml',
             'views/library_book_publisher_menu.xml',
             'demo/demo.xml',
             ],
    'installable': True,
    'auto_install': False,
    'application': True,
    'images':'static/description/icon.png'
}

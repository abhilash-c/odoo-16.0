# -*- coding: utf-8 -*-

{
    'name': 'Sale Invoice',
    'author': 'abhilash',
    'version': '16.0.1.0.0',
    'category': 'Book',
    'depends': ['base', 'account', 'sale_management'],
    'description': "A collection or group of collections of books and/or other print or nonprint materials organized "
                   "and maintained for use reading, consultation, study, research, etc.",
    'data': [
             'views/sale_invoice_views.xml',
             ],
    'installable': True,
    'auto_install': False,
    'application': True,
    # 'images':'static/description/icon.png'
}

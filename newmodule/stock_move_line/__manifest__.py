# -*- coding: utf-8 -*-

{
    'name': 'Stock Move Line',
    'version': '16.0.1.0.0',
    'summary': 'Enhance stock move line functionality for better inventory management.',
    'description': """
        This module extends the functionality related to stock move lines.
        Add custom views and features to enhance the stock management process.
    """,
    'category': 'Inventory/Logistics',
    'author': 'Abhilash',
    'website': 'https://www.example.com',
    'depends': ['base', 'sale_management'],
    'data': [
        'views/stock_move_line_views.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}


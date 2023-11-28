# -*- coding: utf-8 -*-

{
    'name': 'Maintenance Tags',
    'author': 'abhilash',
    'version': '16.0.1.0.0',
    'summary': 'Maintenance & Tags',
    'category': 'Maintenance',
    'website': 'https://www.odoo.com/app/maintenance',
    'depends': ['base', 'maintenance'],
    'description': 'Maintenance tags updation',
    'data': ['security/ir.model.access.csv',
             'views/maintenance_tags_views.xml',
             'views/maintenance_request_views.xml',
             'wizard/update_tags_wizard_views.xml',
             'data/ir_action_data.xml',
             'views/maintenance_menu.xml',],
    'installable': True,
    'auto_install': False,
    'application': True,
    'images':'static/description/icon_image.png'
}

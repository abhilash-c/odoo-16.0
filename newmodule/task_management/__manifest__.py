# -*- coding: utf-8 -*-
{
    'name': 'Task Management',
    'author': 'abhilash',
    'version': '16.0.1.0.0',
    'category': 'Technical',
    'depends': ['base'],
    'description': "Task Manager",
    'data': ['security/ir.model.access.csv',
             'views/task_views.xml',
             'views/task_menus.xml',
             'views/task_notes_views.xml',
             'views/task_users_views.xml'
             ],
    'installable': True,
    'auto_install': False,
    'application': True,
}
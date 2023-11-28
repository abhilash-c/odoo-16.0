# -*- coding: utf-8 -*-

{
    'name': 'EMPLOYEE',
    'author': 'Abhilash',
    'version': '16.0.1.0.0',
    'category': 'Technically',
    'depends': ['base', 'hr'],
    'description':"Employees",
    'data': ['security/ir.model.access.csv',
             # 'security/employee_access.xml',
             # 'security/manager_access.xml',
             'views/employee_views.xml',
             'views/department_views.xml',
             'report/employee_report.xml',
             'views/hr_job_inherit_views.xml',
             'wizard/wizard_review.xml',
             'views/employee_menus.xml',],
    'installable': True,
    'auto_install': False,
    'application': True,
}

# -*- coding: utf-8 -*-
from odoo import models, fields


class EmployeeManagement(models.Model):
    _name = "employee.management"
    _description = "employee"

    first_name = fields.Char(string="First Name", required=True)
    last_name = fields.Char(string="Last Name", required=True)
    email = fields.Char(string="Email")
    phone = fields.Char(string="Phone")
    department = fields.Many2one("department", string="Department")
    hire_date = fields.Date(string="Hire Date")
    salary = fields.Float(string="Salary")
    employees_ids = fields.One2many("review", "review_id", string="employee ids")
    employee_note = fields.Text(string="Employee Note")

    def add_review(self):
        wizard = (self.env['wizard.reviews'].create({
            'review_id': self.id
        }))
        return {
            'name': 'wizard reviews action',
            'type': 'ir.actions.act_window',
            'res_model': 'wizard.reviews',
            'view_mode': 'form',
            'res_id': wizard.id,
            'target': 'new'
        }

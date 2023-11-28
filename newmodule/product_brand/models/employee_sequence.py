from odoo import models, fields, api


class InheritEmployee(models.Model):
    _inherit = 'hr.employee'

    employee_code = fields.Char(string='Employee Code', readonly=True, default='New', copy=False)

    @api.model
    def create(self, vals_list):
        vals_list['employee_code'] = self.env['ir.sequence'].next_by_code('employee_code') or 'New'
        return super(InheritEmployee, self).create(vals_list)

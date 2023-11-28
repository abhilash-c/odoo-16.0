# -*- coding: utf-8 -*-
from odoo import fields, models, api


class CustomProject(models.Model):
    _inherit = "project.project"

    project_code = fields.Char(string='Project Code', readonly=True, default='New', copy=False)

    @api.model
    def create(self, vals_list):
        vals_list['project_code'] = self.env['ir.sequence'].next_by_code('project_code') or 'New'
        return super(CustomProject, self).create(vals_list)

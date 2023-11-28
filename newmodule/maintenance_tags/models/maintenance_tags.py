# -*- coding: utf-8 -*-
from odoo import fields, models


class MaintenanceTags(models.Model):
    _name = 'maintenance.tags'
    _description = 'maintenance tags'

    name = fields.Char(string="Name", required=True)
    code = fields.Char(string="Code")

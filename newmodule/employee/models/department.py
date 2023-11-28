# -*- coding: utf-8 -*-
from odoo import models, fields


class Department(models.Model):
    _name = "department"
    _description = "department"

    name = fields.Char(string="Name")

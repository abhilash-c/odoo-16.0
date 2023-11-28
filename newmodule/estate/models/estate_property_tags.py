# -*- coding: utf-8 -*-
from odoo import models, fields


class EstatePropertyTags(models.Model):
    _name = 'estate.property.tags'
    _description = "Property Tags"
    _order = "name"

    name = fields.Char(string="Name", required=True, store=True)
    color = fields.Integer(string="Color")

    _sql_constraints = [
        ('unique_tag_name', 'UNIQUE(name)', 'Tag name must be unique.')
    ]

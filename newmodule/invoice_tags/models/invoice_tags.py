# -*- coding: utf-8 -*-
from odoo import fields, models


class InvoiceTags(models.Model):
    _name = 'invoice.tags'

    name = fields.Char(string='Name')

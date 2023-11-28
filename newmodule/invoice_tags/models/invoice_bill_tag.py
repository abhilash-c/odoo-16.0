# -*- coding: utf-8 -*-
from odoo import fields, models, api


class InvoiceBillTags(models.Model):
    _inherit = 'account.move'

    tag_ids = fields.Many2many('invoice.tags', string='Tags')

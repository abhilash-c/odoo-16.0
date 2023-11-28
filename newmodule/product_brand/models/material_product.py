# -*- coding: utf-8 -*-

from odoo import models, fields, api


class MaterialProducts(models.Model):
    _name = "material.product"

    customer_name_id = fields.Many2one("res.partner", string="Customer Name")
    collection_date = fields.Date(string="Date")
    customer_type_ids = fields.One2many("material.list", "list_id", string="Customer Type")
    grand_total = fields.Float(string="Grand Total", compute='_compute_grand_total')

    @api.depends('customer_type_ids')
    def _compute_grand_total(self):
        for record in self:
            record.grand_total = sum(record.customer_type_ids.mapped('total'))

# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class SchoolAccessories(models.Model):
    _name = "school.accessories"

    customer_name_id = fields.Many2one('res.partner', string="Customer Name", required=True)
    date = fields.Date(string="Date")
    customer_type_ids = fields.One2many("cloth.list", "list_id", string="Customer Type")
    grand_total = fields.Float(string="Grand Total", compute='_compute_grand_total')

    @api.depends('customer_type_ids')
    def _compute_grand_total(self):
        for record in self:
            record.grand_total = sum(record.customer_type_ids.mapped('total'))

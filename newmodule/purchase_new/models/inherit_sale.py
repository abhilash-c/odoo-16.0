# -*- coding: utf-8 -*-
from odoo import fields, models


class InheritSale(models.Model):
    _inherit = 'sale.order.line'

    mrp = fields.Float(string='mrp', help='Enter the mrp', related="product_id.mrp")
    list_price = fields.Float(string="sales price", related="product_id.list_price")
    # brand_name = fields.Char(string="Brand Name", required=True, related='product_id.brands')

    def sale_order_line_history(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Sale Order Line History',
            'view_mode': 'tree',
            'res_model': 'sale.order.line',
            'target': 'new',
            'domain': ['&', ('product_template_id', '=', self.product_id.name),
                       ('order_partner_id', '=', self.order_id.partner_id.id)]}

# -*- coding: utf-8 -*-

from odoo import models, fields


class ProductPurchaseSale(models.Model):
    _inherit = 'purchase.order.line'

    brand_name = fields.Char(string="Brand Name", required=True, related='product_id.brands')







# -*- coding: utf-8 -*-
from odoo import fields, models, api, exceptions


class InheritPurchase(models.Model):
    _inherit = 'product.template'

    mrp = fields.Float(string='mrp', help='Enter the mrp')
    list_price = fields.Float(string="sales price")
    product_code = fields.Char(string='Product Code', readonly=True, default='New', copy=False)

    # @api.constrains('list_price', 'mrp')
    # def _check_sale_price_mrp(self):
    #     for product in self:
    #         if product.list_price > product.mrp:
    #             raise exceptions.ValidationError("sales price do not exceed mrp")
    #         elif product.list_price <= 0:
    #             raise exceptions.ValidationError("Price field must be positive")
    #         elif product.mrp <= 0:
    #             raise exceptions.ValidationError("mrp must be positive")

    @api.model
    def create(self, vals_list):
        vals_list['product_code'] = self.env['ir.sequence'].next_by_code('product_code') or 'New'
        return super(InheritPurchase, self).create(vals_list)


class ProductPurchaseSale(models.Model):
    _inherit = 'purchase.order.line'

    sale_image = fields.Image(string='image', related='product_id.image_1920')
    mrp = fields.Float(string='mrp', help='Enter the mrp', related="product_id.mrp")
    list_price = fields.Float(string="sales price", related="product_id.list_price")



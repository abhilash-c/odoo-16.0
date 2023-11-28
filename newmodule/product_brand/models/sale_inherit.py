# -*- coding: utf-8 -*-
from odoo import models, fields, api


class SaleInherit(models.Model):
    _inherit = 'sale.order'

    CUSTOM_FIELD_STATES = {state: [('readonly', False)] for state in {'sale', 'cancel'}}
    date_order = fields.Datetime(string="Order Date", states=CUSTOM_FIELD_STATES, copy=False, required=True)
    current_user = fields.Many2one('res.users', string='Current user', default=lambda self: self.env.user)

    def _prepare_confirmation_values(self):
        return {
            'state': 'sale',
        }
    #
    # def action_confirm(self):
    #     super(SaleInherit, self).action_confirm()
    #
    #     out_of_stock_products = self.order_line.filtered(
    #         lambda line: line.product_id.virtual_available < line.product_uom_qty)
    #     print("1 working")
    #
    #     if out_of_stock_products:
    #         template = self.env.ref('product_brand.stock_template_custom')
    #         template.send_mail(self.id, force_send=True)
    #         print("2 working....")

    def action_confirm(self):
        purchase_order_ids = []
        for record in self:
            for res in record.order_line:
                if res.available_qty < res.product_uom_qty:
                    template = self.env.ref('product_brand.stock_template_custom')
                    template.send_mail(self.id, force_send=True)

                    purchase_order = self.env['purchase.order'].create({
                        'partner_id': res.product_id.id,
                        'order_line': [(0, 0, {
                            'product_id': res.product_id.id,
                            'product_qty': res.product_uom_qty - res.available_qty,
                            'price_unit': res.product_id.list_price,
                        })],
                    })
                    purchase_order_ids.append(purchase_order.id)
                    return purchase_order_ids
                break

            super(SaleInherit, self).action_confirm()


class SaleOrderInherit(models.Model):
    _inherit = 'sale.order.line'

    available_qty = fields.Float(related="product_id.qty_available")
    brand_name = fields.Char(string="Brand Name", required=True, related='product_id.brands')

# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class FoodProducts(models.Model):
    _name = "food.products"

    customer_name_id = fields.Many2one('res.partner', string="Customer Name", required=True)
    date = fields.Date(string="Date")
    customer_type_ids = fields.One2many('food.items', 'items_id', string="Food Item")
    grand_total = fields.Float(string="Grand Total", compute='_compute_grand_total')
    current_user = fields.Many2one('res.users', string='Current user', default=lambda self: self.env.user)

    @api.depends('customer_type_ids')
    def _compute_grand_total(self):
        for record in self:
            record.grand_total = sum(record.customer_type_ids.mapped('total'))

    def send_email(self):
        for record in self:
            recipient_email = record.customer_name_id.email
            if recipient_email:
                mail_template = self.env.ref('product_brand.email_template_custom')
                mail_template.send_mail(record.id, force_send=True, email_values={'email_to': recipient_email})
                print(f"Email sent to {recipient_email}")
            else:
                print('No recipient email found for', record.customer_name_id.name)

    def open_product(self):
        wizard = self.env['food.product.wizard'].create({
            'customer_na': self.customer_name_id.name
        })
        return {
            'name': _('Food Product'),
            'type': 'ir.actions.act_window',
            'res_model': 'food.product.wizard',
            'view_mode': 'form',
            'res_id': wizard.id,
            'target': 'new'
        }

# -*- coding: utf-8 -*-
from odoo import models, fields


class TemplateInherit(models.Model):
    _inherit = 'product.template'

    product_brand_id = fields.Many2one("product.brand", string="Product Brand")
    brands = fields.Char(string="Brand", related='product_brand_id.brand_name')

    def open_template(self):
        wizard = (self.env['product.template.wizard'])
        return {
            'name': 'template_wizard_action',
            'type': 'ir.actions.act_window',
            'res_model': 'product.template.wizard',
            'view_mode': 'form',
            'res_id': wizard.id,
            'target': 'new'
        }

from odoo import fields, models, api


class TemplateWizard(models.TransientModel):
    _name = 'product.template.wizard'

    product_id = fields.Many2one('product.product', string='Product', required=True)
    list_price = fields.Float(string="Sales price")

    def update_price(self):
        self.product_id.list_price = self.list_price
        return {'type': 'ir.actions.act_window_close'}

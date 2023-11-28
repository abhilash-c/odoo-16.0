from odoo import models, fields


class InheritInvoice(models.Model):
    _inherit = 'account.move'

    def action_post(self):
        payment = []
        super(InheritInvoice, self).action_post()
        for record in self:
            for res in record.line_ids:
                account_payment = self.env['account.payment'].create({
                        'partner_id': record.partner_id.id,
                        'amount': record.amount_total,
                        'name': record.payment_reference,
                    })
                payment.append(account_payment.id)
                break
        return payment


class AccountLine(models.Model):
    _inherit = 'account.move.line'

    mrp = fields.Float(string='mrp', help='Enter the mrp', related="product_id.mrp")
    sale_price = fields.Float(string="Sale Price",  related="product_id.list_price")
    brand_name = fields.Char(string="Brand Name", required=True, related='product_id.brands')

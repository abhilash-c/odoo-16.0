from odoo import models, Command


class InheritEstate(models.Model):
    _inherit = 'estate.property'

    def action_sold(self):
        print("Working")
        result = super(InheritEstate, self).action_sold()

        discount = self.selling_price * 0.06

        invoice = {
            'partner_id': self.buyer_id.id,
            'move_type': 'out_invoice',
            'journal_id': 1,
            'line_ids': [
                Command.create({
                    'name': self.name,
                    'quantity': 1.0,
                    'price_unit': self.selling_price,
                    'discount': self.discount,
                }),

                Command.create({
                    'name': 'Administrative fees',
                    'quantity': 1.0,
                    'price_unit': 100,
                })
            ],
        }

        report = self.env['account.move'].create(invoice)

        return result

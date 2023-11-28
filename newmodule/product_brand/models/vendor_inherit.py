from odoo import models, fields, api


class InheritVendor(models.Model):
    _inherit = 'res.partner'

    approval_state = fields.Selection([('waiting', 'Waiting'), ('approved', 'Approved')], string='Approval State',
                                      default='waiting')
    customer_number = fields.Char(string='Unique Number', readonly=True, default='New', copy=False)

    @api.model
    def create(self, vals_list):
        result = super(InheritVendor, self).create(vals_list)
        customer_rank = vals_list.get('customer_rank')
        supplier_rank = vals_list.get('supplier_rank')

        if customer_rank is not None and customer_rank > 0:
            vals_list['customer_number'] = self.env['ir.sequence'].next_by_code('res.partner.sequence') or 'New'

        elif supplier_rank is not None and supplier_rank > 0:
            vals_list['customer_number'] = self.env['ir.sequence'].next_by_code('vendor_res.partner.sequence') or 'New'

        result = super(InheritVendor, self).create(vals_list)
        return result


class ProductMaster(models.Model):
    _inherit = 'product.supplierinfo'

    partner_id = fields.Many2one(
        'res.partner', 'Vendor',
        ondelete='cascade', required=True,
        check_company=True, domain=[('approval_state', '=', 'approved'), ('supplier_rank', '=', 1)])

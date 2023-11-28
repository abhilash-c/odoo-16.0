# -*- coding: utf-8 -*-
from odoo import fields, models, api


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    amount_total_signed = fields.Monetary(string='Invoiced Amount', compute='_compute_invoice_amounts', store=True)
    amount_residual = fields.Monetary(string='Amount Due', compute='_compute_invoice_amounts', store=True)
    amount_paid = fields.Monetary(string='Amount Paid', compute='_compute_amount_paid', store=True)

    @api.depends('invoice_ids.amount_total_signed', 'invoice_ids.amount_residual', 'invoice_ids.state')
    def _compute_invoice_amounts(self):
        for record in self:
            non_canceled_invoices = record.invoice_ids.filtered(lambda invoice: invoice.state != 'cancel')

            record.amount_total_signed = sum(non_canceled_invoices.mapped('amount_total_signed'))
            record.amount_residual = sum(non_canceled_invoices.mapped('amount_residual'))

    @api.depends('amount_total_signed', 'amount_residual')
    def _compute_amount_paid(self):
        for record in self:
            record.amount_paid = record.amount_total_signed - record.amount_residual

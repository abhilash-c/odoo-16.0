# -*- coding: utf-8 -*-
from odoo import models, fields, api


class StockMoveLine(models.Model):
    _inherit = 'sale.order'

    stock_move_line_ids = fields.Many2many('stock.move.line', string='Sale Order Lines',
                                           compute='_compute_stock_move_lines')

    @api.depends('picking_ids')
    def _compute_stock_move_lines(self):
        for order in self:
            line_ids = []
            for picking in order.picking_ids.mapped('move_line_ids'):
                line_ids.append(picking.id)
            order.stock_move_line_ids = line_ids

    # @api.depends('picking_ids')
    # def _compute_stock_move_lines(self):
    #     for order in self:
    #         order.stock_move_line_ids = [picking.id for picking in order.picking_ids.mapped('move_line_ids')]

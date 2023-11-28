# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ClothList(models.Model):
    _name = "cloth.list"

    name = fields.Char(string="Name", required=True)
    type_of_cloth = fields.Selection([('cotton', 'COTTON'), ('silk', 'SILK'), ('polyster', 'POLYSTER')],
                                     string="Clothes")
    quantity = fields.Integer(string="Quantity", required=True)
    code = fields.Char(string="Code")
    amount = fields.Float(string="Amount", required=True)
    total = fields.Float(string="Total", compute="_compute_total")
    list_id = fields.Many2one("cloth.product", string="list id")

    @api.depends("amount", "quantity")
    def _compute_total(self):
        for record in self:
            record.total = record.amount * record.quantity

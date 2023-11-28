# -*- coding: utf-8 -*-

from odoo import models, fields, api


class FoodItems(models.Model):
    _name = "food.items"

    name = fields.Char(string="Name", required=True)
    quantity = fields.Integer(string="Quantity", required=True)
    code = fields.Char(string="Code")
    amount = fields.Float(string="Amount", required=True)
    total = fields.Float(string="Total", compute="_compute_total")
    items_id = fields.Many2one('food.products', string="Items")

    @api.depends("amount", "quantity")
    def _compute_total(self):
        for record in self:
            record.total = record.amount * record.quantity

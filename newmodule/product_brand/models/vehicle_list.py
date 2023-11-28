# -*- coding: utf-8 -*-

from odoo import models, fields, api


class VehicleList(models.Model):
    _name = "vehicle.list"

    name = fields.Char(string="Name", required=True)
    quantity = fields.Integer(string="Quantity", required=True)
    code = fields.Char(string="Code")
    amount = fields.Float(string="Amount", required=True)
    total = fields.Float(string="Total", compute="_compute_total")
    list_id = fields.Many2one("vehicle.product", string="list id")

    @api.depends("amount", "quantity")
    def _compute_total(self):
        for record in self:
            record.total = record.amount * record.quantity

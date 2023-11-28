# -*- coding: utf-8 -*-
from odoo import models, fields
from datetime import datetime, timedelta


class LaundaryManagement(models.Model):
    _name = "laundary.management"
    _description = "laundary"

    clothes = fields.Selection([('cotton', 'COTTON'), ('silk', 'SILK'), ('polyster', 'POLYSTER')], string="Clothes")
    customer = fields.Many2one("res.partner", string="Customer")
    date = fields.Date(string="Date", default=lambda self: (datetime.today()))
    Amount = fields.Float(string="Amount")
    delivery_date = fields.Datetime(string="Delivery_Date", default=lambda self: (datetime.today() +
                                                                                  timedelta(days=10)))
    quantity = fields.Float(string="Quantity")
    contact = fields.Char(string="Contact")
    postcode = fields.Char(string="Postcode")
    
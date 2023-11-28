# -*- coding: utf-8 -*-
from odoo import fields, models


class LibraryBookCategory(models.Model):
    _inherit = 'library.book.category'
    _description = 'library book category'

    max_borrow_days = fields.Integer(string="Borrow Days", default=10)

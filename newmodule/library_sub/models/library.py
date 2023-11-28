# -*- coding: utf-8 -*-
from odoo import fields, models
from datetime import datetime, timedelta


class Library(models.Model):
    _inherit = 'library.book'
    _description = 'library book'

    date_return = fields.Date(string="Return Date")

    def make_borrowed(self):
        for record in self:
            record.date_return = datetime.today() + timedelta(days=self.book_category_id.max_borrow_days)
        return super(Library, self).make_borrowed()

    def make_available(self):
        for record in self:
            record.date_return = False
        return super(Library, self).make_available()

# -*- coding: utf-8 -*-
from odoo import fields, models


class RentBookWizard(models.TransientModel):
    _name = 'rent.book.wizard'
    _description = 'rent book wizard'

    borrower_id = fields.Many2one('res.partner', string="Borrower")
    book_ids = fields.Many2many('library.book', string='Books', domain="[('status', '=', 'available')]")

    def rent_book(self):
        for rec in self:
            for book in rec.book_ids:
                book.rent_this_book()

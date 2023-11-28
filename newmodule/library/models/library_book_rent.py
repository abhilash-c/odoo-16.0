# -*- coding: utf-8 -*-
from odoo import models, fields, api
from datetime import date
from odoo.exceptions import UserError


class LibraryBookRent(models.Model):
    _name = 'library.book.rent'
    _description = 'library book rent'
    _rec_name = 'book_id'

    book_id = fields.Many2one("library.book", string="Book", required=True)
    borrower = fields.Many2one("res.partner", string="Borrower")
    state = fields.Selection([('ongoing', 'Ongoing'), ('returned', 'Returned'), ('lost', 'Lost')], string='State',
                             default='ongoing', required=True, help='The current state of the book')
    rent_date = fields.Date(string="Rent Date", default=lambda self: (date.today()))
    return_date = fields.Date(string="Return Date")

    def return_the_book(self):
        for rec in self:
            if rec.state == 'ongoing':
                rec.state = 'returned'
                rec.book_id.status = 'available'
                rec.return_date = rec.rent_date

    @api.onchange('book_id')
    def _onchange_book(self):
        for rec in self:
            if rec.book_id:
                rec.book_id.status = 'borrowed'

    def mark_as_lost(self, lost_action=False):
        for rec in self:
            if rec.state in ('ongoing', 'returned'):
                rec.book_id.with_context(update_active=lost_action).sudo().make_lost()
                rec.sudo().write({
                    'state': 'lost',
                })

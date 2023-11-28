# -*- coding: utf-8 -*-
from odoo import fields, models, api


class ReturnBook(models.TransientModel):
    _name = 'return.book'
    _description = 'return book'

    borrowers_id = fields.Many2one('res.partner', string="Borrower")
    books_ids = fields.Many2many('library.book', string='Books')
    type_id = fields.Many2one('library.book.rent', string="type")

    @api.onchange('borrowers_id')
    def _onchange_borrower_id(self):
        for rec in self:
            if rec.borrowers_id:
                my_list = []
                temp = self.env['library.book.rent']
                for record in temp.search([('borrower', '=', rec.borrowers_id.id), ('state', '=', 'ongoing')]):
                    my_list.append(record.book_id.id)
                rec.books_ids = my_list

    # def return_book(self):
    #     for rec in self:
    #         for book in rec.books_ids:
    #             book.borrower_id.return_the_book()

    # def return_book(self):
    #     for rec in self:
    #         for book in rec.books_ids:
    #             book.borrower_id.return_the_book()

    def return_book(self):
        for rec in self:
            for book in rec.books_ids:
                rent = rec.env['library.book.rent'].search([
                    ('book_id', '=', book.id)
                ])
                rent.return_the_book()


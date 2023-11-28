# -*- coding: utf-8 -*-
from odoo import models, fields


class LibraryPublishedBooks(models.Model):
    _name = 'published.books'
    _description = 'published books'

    name_id = fields.Many2one('library.book', string='Name', required=True)
    release_date = fields.Date(string='Release Date')
    publisher_id = fields.Many2one('book.publisher', required=True, string='Publisher')

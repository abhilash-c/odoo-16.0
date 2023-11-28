# -*- coding: utf-8 -*-
from odoo import models, fields


class BookPublisher(models.Model):
    _name = 'book.publisher'
    _description = 'book publisher'

    name = fields.Char(string='name')
    published_books_ids = fields.One2many('published.books', 'publisher_id', string='Published Books')
    email = fields.Char(string='Email')
    phone_number = fields.Char(string='Phone number')

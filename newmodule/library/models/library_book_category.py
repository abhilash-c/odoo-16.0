# -*- coding: utf-8 -*-
from odoo import models, fields


class LibraryBookCategory(models.Model):
    _name = 'library.book.category'
    _description = 'library book category'

    name = fields.Char(string="Name")
    parent_category_id = fields.Many2one("library.book.category", string="Parent Category")
    child_categories_ids = fields.One2many("library.book.category", "parent_category_id", string="Child Category")
    description = fields.Text(string="Description")

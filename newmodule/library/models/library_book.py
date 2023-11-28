# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from datetime import date, timedelta
from odoo.exceptions import ValidationError, UserError


class Library(models.Model):
    _name = 'library.book'
    _description = 'Library Book'
    _rec_name = 'title'

    title = fields.Char(string='Title', required=True, help='The title of the book')
    short_title = fields.Char(string='Short Title', help='A shorter version of book title')
    release_date = fields.Date(string='Release Date', required=True, help='The date when the book was published')
    internal_notes = fields.Text(string='Internal Notes', help='Additional information about book')
    status = fields.Selection([('draft', 'Unavailable'), ('available', 'Available'), ('lost', 'Lost'),
                               ('borrowed', 'Borrowed')], string='Status',
                              default='available',  help='The current status of the book')
    out_of_print = fields.Boolean(string='Out of Print', default=True, help='Whether the book is out of print or not.')
    num_pages = fields.Integer(string='Number of Pages', required=True, help='Total number of pages in the book')
    reader_rating = fields.Float(string='Reader Rating', help='The average rating given by the readers')
    retail_prices = fields.Monetary(string='Retail Price', help='The retail price of the book')
    currency_id = fields.Many2one("res.currency", string='Currency')
    publisher_id = fields.Many2one('book.publisher', string='Publisher')
    librarian_id = fields.Many2one('res.users', string='Librarian')
    author_ids = fields.Many2many('res.partner', string='Author')
    email = fields.Char(string='Email', related='publisher_id.email')
    phone_number = fields.Char(string='Phone number', related='publisher_id.phone_number')
    age_days = fields.Integer(string="Age Days", compute='_compute_age_days', inverse='_inverse_age_days',
                              search='_search_age_days')
    current_date = fields.Date(string='Date', default=lambda self: (date.today()))
    book_category_id = fields.Many2one("library.book.category", string="Book Category")
    author_names = fields.Text(string="Author Names")
    manager_remarks = fields.Char(string="Manager Remarks")
    isbn_numbers = fields.Char(string="Isbn Number")
    borrower_id = fields.Many2one("library.book.rent")
    old_edition_id = fields.Many2one("library.book", string="Old edition", index=True)
    active = fields.Boolean(string="Active", default=True)

    @api.depends('release_date', 'current_date')
    def _compute_age_days(self):
        for rec in self:
            if rec.release_date and rec.current_date:
                rec.age_days = (rec.current_date - rec.release_date).days

    def _inverse_age_days(self):
        for record in self:
            if record.age_days and record.current_date:
                record.release_date = record.current_date - timedelta(days=record.age_days)

    @api.model
    def _search_age_days(self, operator, value):
        age = date.today() - timedelta(days=value)
        return [('release_date', operator, age)]

    @api.constrains('release_date')
    def _onchange_price(self):
        for rec in self:
            if rec.release_date and rec.release_date > rec.current_date:
                raise ValidationError("Release date do not exceed current date")

    @api.depends('title', 'release_date')
    def name_get(self):
        combination = []
        for category in self:
            name = category.title + "(" + str(category.release_date) + ")" + ','.join(category.author_ids.mapped('name'))
            combination.append((category.id, name))
        return combination

    _sql_constraints = [
        ('check_title', 'UNIQUE(title)', 'Book title must be unique'),
        ('check_num_pages', 'CHECK(num_pages >= 0)', 'The number of pages must be positive')
    ]

    def make_available(self):
        for rec in self:
            if rec.status in ('draft', 'borrowed', 'lost'):
                rec.status = 'available'
            else:
                raise ValidationError("Already Available")

    def make_borrowed(self):
        for rec in self:
            if rec.status == 'available':
                rec.status = 'borrowed'
            else:
                raise ValidationError("Only available properties can be borrowed")

    def make_lost(self):
        if self._context.get('update_active', True):
            self.write({
                'active': False,
            })
        self.sudo().write({
            'status': 'lost',
        })

    def get_author_names(self):
        if self.author_ids:
            author_names = ','.join(self.author_ids.mapped('name'))
            self.author_names = author_names

    def create_category(self):
        if self.book_category_id:
            category = self.env['library.book.category'].create({
                'name': "me",
                'description': 'Descriptions',
                'parent_category_id': self.book_category_id.id,
                'child_categories_ids': [(0, 0, {
                    'name': "something",
                    'description': 'Descriptions',
                })],
            })
            return category

    def update_date(self):
        for rec in self:
            if rec.release_date:
                rec.release_date = fields.Date.today()

    @api.model
    def name_search(self, name, args=None, operator='ilike', limit=100):
        partners = self.search(['|', '|', ('title', operator, name), ('isbn_numbers', operator, name),
                                ('author_ids', operator, name)])
        return partners.name_get()

    def write(self, val_list):
        user = self.env.user
        if val_list.get('manager_remarks'):
            if user.has_group('library.normal_user_access'):
                raise UserError('You Cannot Edit the Field Remarks')
        return super(Library, self).write(val_list)

    @api.model
    def create(self, val_list):
        user = self.env.user
        if val_list.get('manager_remarks'):
            if user.has_group('library.normal_user_access'):
                raise UserError('You Cannot Create the Field Remarks')
        return super(Library, self).create(val_list)

    def rent_this_book(self):
        for rec in self:
            if rec.status != 'available':
                raise UserError("Book not available for renting")
            if rec.status == 'available':
                rec.sudo().write({
                    'status': "borrowed"
                })
                book_rent = rec.env['library.book.rent'].sudo().create({
                    'book_id': rec.id,
                    'borrower': self.env.user.partner_id.id
                })
                return book_rent

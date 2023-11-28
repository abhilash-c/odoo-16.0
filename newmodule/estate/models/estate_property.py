# -*- coding: utf-8 -*-
from odoo import models, fields, api, exceptions
from datetime import datetime, timedelta
from odoo.exceptions import ValidationError
from odoo.tools.float_utils import float_compare, float_is_zero


class EstateProperty(models.Model):
    _name = "estate.property"
    _description = 'property'
    _order = "id desc"

    name = fields.Char(string='Name', required=True, help='Enter the name')
    postcode = fields.Char(string='Postcode', help='postal code of location')
    description = fields.Text(string='Description', help="Description of the property")
    date_availability = fields.Date(string='Date availability', default=lambda self: (datetime.today() +
                                                                                      timedelta(days=90)),
                                    copy=False, help='Date availability')
    expected_price = fields.Float(string='Expected Price', required=True, help='Expected selling price')
    selling_price = fields.Float(string='Selling Price', readonly=True, copy=False, help='Actual selling price')
    bedrooms = fields.Integer(string='Bedrooms', default=2, help='Number of bedrooms')
    living_area = fields.Integer(string='Living area', help='Total living area')
    facades = fields.Integer(string='Facades', help='Number of facades')
    garage = fields.Boolean(string='Garage', default=True, help='Whether there is garage')
    garden = fields.Boolean(string='Garden', default=True, help='Whether there is garden')
    garden_area = fields.Integer(string='Garden area', help='Total area of garden')
    garden_orientation = fields.Selection([
        ('north', 'North'),
        ('south', 'South'),
        ('east', 'East'),
        ('west', 'West'),
        ('northeast', 'Northeast'),
        ('northwest', 'Northwest'),
        ('southeast', 'Southeast'),
        ('southwest', 'Southwest'),
        ('other', 'Other')
    ], string='Garden Orientation',  help='Orientation of garden')
    active = fields.Boolean(string='Active', default=True, help='Whether the property is active or not')
    state = fields.Selection([('new', 'New'), ('offer_received', 'Offer Received'),
                              ('offer_accepted', 'Offer Accepted'), ('sold', 'Sold'), ('canceled', 'Canceled'), ],
                             string='State', required=True, default='new', copy=False, readonly=True)
    property_type_id = fields.Many2one('estate.property.type', string='Property Type')
    buyer_id = fields.Many2one('res.partner', copy=False, string='Buyer')
    seller_id = fields.Many2one('res.users', default=lambda self: self.env.user, string='Seller')
    property_tags_ids = fields.Many2many('estate.property.tags', string='Property Tags')
    offer_ids = fields.One2many('estate.property.offer', 'property_id', string='Offers')
    code = fields.Char(related='property_type_id.code', store=True, string='Code')
    total_area = fields.Integer(compute="_compute_total_area", string='Total area (sqm)')
    best_offer = fields.Char(compute='_compute_best_offer', string='Best Offer')
    discount = fields.Float(string="Discount")
    test = fields.Integer(string="Test", default=0)

    @api.depends("living_area", "garden_area")
    def _compute_total_area(self):
        for record in self:
            record.total_area = record.living_area + record.garden_area

    @api.depends("offer_ids")
    def _compute_best_offer(self):
        for record in self:
            if record.offer_ids:
                record.best_offer = max(record.offer_ids.mapped('price'))
            else:
                record.best_offer = 0.0

    @api.onchange('garden')
    def _onchange_garden(self):
        if self.garden:
            self.garden_area = 10.0
            self.garden_orientation = 'north'
        else:
            self.garden_area = 0.0
            self.garden_orientation = False

    def action_cancel(self):
        for record in self:
            if record.state == 'sold':
                raise exceptions.UserError("Cannot cancel a property that is already sold.")
            record.state = 'canceled'

    def action_sold(self):
        for record in self:
            if record.state == 'canceled':
                raise exceptions.UserError("Cannot mark a canceled property as sold.")
            record.state = 'sold'
            if record.state == 'sold':
                record.test = 1
                print(record.test)

    _sql_constraints = [
        ('check_expected_price', 'CHECK(expected_price >= 0)', 'The expected price must be strictly positive'),
        ('check_selling_price', 'CHECK(selling_price >= 0)', 'The selling price must be strictly positive')
    ]

    @api.constrains('selling_price', 'expected_price')
    def _check_selling_price(self):
        for record in self:
            if not float_is_zero(record.selling_price, precision_digits=2):
                threshold = record.expected_price * 0.9
                if float_compare(record.selling_price, threshold, precision_digits=2) < 0:
                    raise ValidationError("The selling price must be at least 90% of the expected price.")

    @api.ondelete(at_uninstall=False)
    def property_delete(self):
        for record in self:
            if record.state not in ['New', 'Canceled']:
                raise exceptions.UserError("cannot delete property with states 'New' or 'Canceled")

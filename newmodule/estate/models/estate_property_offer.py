# -*- coding: utf-8 -*-
from odoo import models, fields, api, exceptions
from datetime import timedelta


class EstatePropertyOffer(models.Model):
    _name = "estate.property.offer"
    _description = "Property Offer"
    _order = "price desc"

    price = fields.Float(string='Price')
    property_id = fields.Many2one('estate.property', required=True,
                                  widget="many2one")
    status = fields.Selection([('accepted', 'Accepted'), ('refused', 'Refused')],
                              string='Status', copy=False)
    partner_id = fields.Many2one('res.partner', required=True, string="Customer")
    validity = fields.Integer(string='Validity (Date)', default=7)
    date_deadline = fields.Date(string='Deadline', compute='_compute_date_deadline', inverse='_inverse_date_deadline',
                                store=True)
    property_type_id = fields.Many2one('estate.property.type', string='Property Type',
                                       related='property_id.property_type_id', store=True)

    @api.depends('validity')
    def _compute_date_deadline(self):
        for record in self:
            if record.validity:
                record.date_deadline = fields.Date.today() + timedelta(days=record.validity)

    def _inverse_date_deadline(self):
        for record in self:
            if record.date_deadline:
                record.validity = (record.date_deadline - fields.Date.today()).days
            else:
                record.validity = 0

    def action_confirm(self):
        for record in self:
            if record.status == 'accepted':
                raise exceptions.UserError("This offer is already accepted.")
            accepted_offer = self.search([('property_id', '=', record.property_id.id), ('status', '=', 'accepted')])
            if accepted_offer:
                raise exceptions.UserError("Another offer for this property is already accepted.")
            record.property_id.selling_price = record.price
            record.property_id.buyer_id = record.partner_id
            record.status = 'accepted'
            record.property_id.state = 'offer_accepted'

    def action_cancel(self):
        for record in self:
            if record.status == 'refused':
                raise exceptions.UserError("This offer is already refused.")
            record.property_id.selling_price = 0
            record.property_id.buyer_id = None
            record.status = 'refused'

    _sql_constraints = [
        ('check_price', 'CHECK(price >= 0)', 'The offer price must be strictly positive')
    ]

    # @api.constrains('price')
    # def offer(self):
    #     for record in self:
    #         if record.price:
    #             record.property_id.state = "offer_received"

    @api.model
    def create(self, vals):
        existing_offers = self.search([('property_id', '=', vals.get('property_id'))])

        if existing_offers and any(vals.get('price', 0.0) < offer.price for offer in existing_offers):
            raise exceptions.ValidationError("New offer price cannot be lower than an existing offer price.")

        property_id = self.env['estate.property'].browse(vals.get('property_id'))
        property_id.state = 'offer_received'
        return super(EstatePropertyOffer, self).create(vals)

    # @api.model
    # def create(self, vals):
    #     existing_offers = self.search([('property_id', '=', vals.get('property_id'))])
    #     for offer in existing_offers:
    #         if vals.get('price', 0.0) < offer.price:
    #             raise exceptions.ValidationError(
    #                 "New offer price cannot be lower than an existing offer price:{}".format(offer.price))
    #
    #     property_id = self.env['estate.property'].browse(vals.get('property_id'))
    #     property_id.state = 'offer_received'
    #     return super(EstatePropertyOffer, self).create(vals)

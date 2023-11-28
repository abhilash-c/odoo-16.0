# -*- coding: utf-8 -*-
from odoo import models, fields, api


class EstatePropertyType(models.Model):
    _name = 'estate.property.type'
    _description = 'property Type'
    _order = 'sequence, name'

    name = fields.Char(string="Name", required=True)
    code = fields.Char(string="Code", required=True)
    property_ids = fields.One2many("estate.property", "property_type_id", string="Properties")
    sequence = fields.Integer(string="Sequence", help="Used to order stages")
    offer_ids = fields.One2many('estate.property.offer', 'property_type_id', string='Offers')

    _sql_constraints = [
        ('unique_type_name', 'UNIQUE(name)', 'Type name must be unique.')
    ]

    offer_count = fields.Integer(string='Offer Count', compute='_compute_offer_count')

    @api.depends('offer_ids')
    def _compute_offer_count(self):
        for record in self:
            record.offer_count = len(record.offer_ids)

    def action_open_property_offers(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Property Offer',
            'res_model': 'estate.property.offer',
            'view_mode': 'tree',
            'view_id': 'estate.estate_property_view_tree',
            'domain': [('property_type_id', '=', self.name)]
        }

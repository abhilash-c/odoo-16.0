# -*- coding: utf-8 -*-
from odoo import models, fields


class InheritResUsers(models.Model):
    _inherit = 'res.users'

    property_ids = fields.One2many('estate.property', 'seller_id')

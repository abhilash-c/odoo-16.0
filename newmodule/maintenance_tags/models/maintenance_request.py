# -*- coding: utf-8 -*-
from odoo import fields, models


class MaintenanceRequestTags(models.Model):
    _inherit = 'maintenance.request'
    _description = 'maintenance request tags linking'

    tags_ids = fields.Many2many('maintenance.tags', string='Tags')

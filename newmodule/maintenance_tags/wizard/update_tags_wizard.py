# -*- coding: utf-8 -*-
from odoo import fields, models


class UpdateTagsWizard(models.TransientModel):
    _name = 'update.tags.wizard'
    _description = 'tag update wizard'

    tags_ids = fields.Many2many("maintenance.tags", string="Tags")

    def update_tags(self):
        active_ids = self._context.get('active_ids')
        requests = self.env['maintenance.request'].browse(active_ids)

        for rec in requests:
            rec.tags_ids = self.tags_ids
            # rec.write({
            #     'tags_ids': [(6, 0, self.tags_ids.ids)]
            # })

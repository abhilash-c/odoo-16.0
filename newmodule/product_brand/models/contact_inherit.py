# -*- coding: utf-8 -*-

from odoo import models


class Customer(models.Model):
    _inherit = 'res.partner'

    def open_food_items(self):
        return {
            'name': 'Food Items',
            'type': 'ir.actions.act_window',
            'res_model': 'food.items',
            'view_mode': 'tree,form',
            'domain': [('items_id.customer_name_id', 'in', self.ids)],
        }

    def open_material_list(self):
        return {
            'name': 'Material List',
            'type': 'ir.actions.act_window',
            'res_model': 'material.list',
            'view_mode': 'tree,form',
            'domain': [('list_id.customer_name_id', 'in', self.ids)],
        }

    def open_cloth_list(self):
        return {
            'name': 'Material List',
            'type': 'ir.actions.act_window',
            'res_model': 'cloth.list',
            'view_mode': 'tree,form',
            'domain': [('list_id.customer_name_id', 'in', self.ids)],
        }

    def open_vehicle_list(self):
        return {
            'name': 'Vehicle List',
            'type': 'ir.actions.act_window',
            'res_model': 'vehicle.list',
            'view_mode': 'tree,form',
            'domain': [('list_id.customer_name_id', 'in', self.ids)],
        }

    def open_school_list(self):
        return {
            'name': 'School Acc List',
            'type': 'ir.actions.act_window',
            'res_model': 'school.acc.list',
            'view_mode': 'tree,form',
            'domain': [('list_id.customer_name_id', 'in', self.ids)],
        }

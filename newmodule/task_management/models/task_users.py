# -*- coding: utf-8 -*-
from odoo import fields, models


class UsersManagement(models.Model):
    _name = "users.management"

    followers_ids = fields.Many2many("res.users", string="Followers")

# -*- coding: utf-8 -*-
from odoo import models, fields, api


class TaskManagement(models.Model):
    _name = "task.task"
    _description = "Task Management"

    name = fields.Char(string="Name", required=True)
    description = fields.Text(string="description")
    deadline = fields.Date(string="Date")
    priority = fields.Text(string="Priority")
    assigned_id = fields.Many2one("res.users", string="Assigned to")
    task_ids = fields.One2many("note.book", "task_type_id", string="Task_note")





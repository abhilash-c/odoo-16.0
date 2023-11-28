# -*- coding: utf-8 -*-
from odoo import models, fields


class NoteBook(models.Model):
    _name = "note.book"

    task_type_id = fields.Many2one("task.task", string="Task Type")

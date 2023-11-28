# -*- coding: utf-8 -*-
from odoo import models, fields


class InheritHrJob(models.Model):
    _inherit = "hr.job"

    job_description = fields.Text(string="Job Description")

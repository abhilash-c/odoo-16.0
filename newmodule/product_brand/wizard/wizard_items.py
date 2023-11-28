from odoo import fields, models


class FoodProductWizard(models.TransientModel):
    _name = "food.product.wizard"

    customer_na = fields.Char(string="Customer")
    date = fields.Date(string="Date")

from odoo import fields, models


class WizardReviews(models.TransientModel):
    _name = 'wizard.reviews'

    review = fields.Text(string="Review")
    review_id = fields.Many2one("employee.management", string="Review Id")

    def update_review(self):
        demo = {
            'review': self.review,
            'review_id': self.review_id.id
        }
        ret_demo = self.env['review'].create(demo)
        return ret_demo


class Review(models.Model):
    _name = 'review'

    review = fields.Text(string='Review')
    review_id = fields.Many2one('employee.management', string='Reviews id')

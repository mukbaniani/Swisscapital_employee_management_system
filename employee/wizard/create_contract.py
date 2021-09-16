from odoo import models, fields, api
from datetime import date
from odoo.exceptions import ValidationError


class CreateContractWizard(models.TransientModel):
    _name = "create.contract.wizard"
    _description = "create contract wizard"

    create_at = fields.Date(string="შექმნის თარიღი", default=date.today())
    finish_date = fields.Date(string="დასრულების დრო")
    contract_number = fields.Char(string="კონტრაქტის ნომერი")
    employee = fields.Many2one(
        "employee.employee", string="თანამშრომელი", required=True
    )

    @api.constrains("finish_date")
    def _validate_finish_date(self):
        if self.finish_date > self.create_at:
            error_message = "კონტრაქტის დასრულების დრო მეტი უნდა იყოს კონტრაქტის დაწყების დაწყების დროზე"
            raise ValidationError(error_message)

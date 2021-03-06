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
        if self.finish_date < self.create_at:
            error_message = "კონტრაქტის დასრულების დრო მეტი უნდა იყოს კონტრაქტის დაწყების დაწყების დროზე"
            raise ValidationError(error_message)

    def save(self):
        contract_vals = {
            "start_date": self.create_at,
            "end_date": self.finish_date,
            "constract_number": self.contract_number,
        }
        self.env["employee.contract"].create(contract_vals)
        contract = self.env["employee.contract"].search([])[-1]
        self.env["employee.employee"].search([("id", "=", self.employee.id)]).update(
            {"contract": contract}
        )

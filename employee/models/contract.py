from odoo import models, fields


class Contract(models.Model):
    _name = "employee.contract"
    _description = "swisscapital employees contract"

    start_date = fields.Date(string="დაწყების დრო")
    end_date = fields.Date(string="დასრულების დრო")
    constract_number = fields.Char(string="კონტრაქტის ნომერი")

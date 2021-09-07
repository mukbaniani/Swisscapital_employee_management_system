from odoo import models, fields


class Department(models.Model):
    _name = 'department.department'
    _description = 'swisscapital department list'

    name = fields.Char(string="დეპარტემენიტის სახელი", required=True)

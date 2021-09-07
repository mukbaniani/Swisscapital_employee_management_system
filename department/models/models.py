from odoo import models, fields


class Department(models.Model):
    _name = 'department.department'
    _description = 'swisscapital department list'
    _order = 'id desc'

    name = fields.Char(string="დეპარტემენიტის სახელი", required=True)

    _sql_constraints = [ 
        ('name_unique', 'unique(name)', "მსხაგვსი დეპარტამენტი უკვე არსებობს")
    ]

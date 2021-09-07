from odoo import models, fields


class PersonalQuality(models.Model):
    _name = 'personal_quality.personal_quality'
    _description = 'swisscapital employees personal_quality'
    _order = "id desc"

    name = fields.Char(string="პიროვნული თვისებები", required=True)

    _sql_constraints = [ 
        ('name_unique', 'unique(name)', 'მსგავსი პიროვნული თვისება უკვე არსებობს')
    ]

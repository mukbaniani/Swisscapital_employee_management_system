from odoo import models, fields, api


class PersonalQuality(models.Model):
    _name = 'personal_quality.personal_quality'
    _description = 'swisscapital employees personal_quality'

    name = fields.Char(string="პიროვნული თვისებები", required=True)

from datetime import datetime
from odoo import models, fields, api
from odoo.exceptions import ValidationError
import re


TODAY = fields.Date.today()
ADULT = 18


class Employee(models.Model):
    _name = "employee.employee"
    _description = "swisscapital employee management"
    _order = "id desc"

    first_name = fields.Char(string="სახელი", required=True)
    last_name = fields.Char(string="გვარი", required=True)
    citizenship = fields.Char(string="მოქალაქეობა", required=True)
    gender = fields.Selection(
        [("კ", "კაცი"), ("ქ", "ქალი")], required=True, string="სქესი"
    )
    person_number = fields.Char(
        string="პირადი ნომერი", required=True, help="შეიყვანეთ 11 ციფრი"
    )
    date_of_birth = fields.Date(string="დაბადების თარიღი", required=True)
    date_expiry = fields.Date(string="მოქმედების ვადა", required=True)
    card_number = fields.Char(
        string="ბარათის ნომერი",
        required=True,
        help="2 ციფრი 2 დიდი ლათინური ასო 5 ციფრი",
    )
    image = fields.Image(string="სურათი", max_with=100, max_height=100)
    place_of_birth = fields.Char(string="დაბადების ადგილი", required=True)
    date_of_issue = fields.Date(string="გაცემის თარიღი", required=True)
    issueing_authority = fields.Char(string="გამცემი ორგანო", required=True)
    department_id = fields.Many2one(
        "department.department", string="დეპარტამენტი", required=True
    )
    personal_quality = fields.Many2many(
        "personal_quality.personal_quality", string="პიროვნული თვისებები", required=True
    )
    fname_lname = fields.Char(
        string="თანამშრომლის სახელი გვარი", compute="_compute_fname_lname"
    )
    count_age = fields.Char(
        string="თანამშრომლის ასაკი", compute="_compute_date_of_birth", default=""
    )
    personal_quality_list = fields.Char(
        string="პიროვნული თვისებების სია",
        compute="_compute_personal_quality",
        store=True,
    )

    _sql_constraints = [
        (
            "person_number",
            "unique(person_number)",
            "პირადი ნომერი უნდა იყოს უნიკალური მსგავსი პირადი ნომერი უკვე გამოყენებულია",
        ),
    ]

    def count_employee_age(self):
        if self.date_of_birth:
            today = datetime.now()
            bdate = fields.Datetime.to_datetime(self.date_of_birth)
            age = (today - bdate).days / 365.24
            return int(age)

    @api.depends("personal_quality")
    def _compute_personal_quality(self):
        quality_list = ""
        for record in self:
            for quality in record.personal_quality:
                quality_list += f"{quality.name}, "
                record.personal_quality_list = quality_list

    @api.depends("first_name", "last_name")
    def _compute_fname_lname(self):
        if self.first_name and self.last_name:
            self.fname_lname = f"{self.first_name} {self.last_name}"
        else:
            self.fname_lname = ""

    @api.depends("date_of_birth")
    def _compute_date_of_birth(self):
        age = self.count_employee_age()
        self.count_age = f"{age} წლის"

    @api.constrains("person_number")
    def _check_person_number_length(self):
        for record in self:
            if re.match("^[0-9]{11}$", record.person_number) == None:
                raise ValidationError("პირადი ნომერი უნდა შეიცავდეს 11 ციფრს")

    @api.constrains("card_number")
    def _check_card_number_length(self):
        for record in self:
            if re.match("^[0-9]{2}[A-Z]{2}[0-9]{5}$", record.card_number) is None:
                raise ValidationError(
                    "ბარათის ნომერი უნდა შეიცავდეს 9 სიმბოლოს 2 ცირფი 2 დიდი ლათინური ასო 5 ციფრი"
                )

    @api.constrains("date_of_birth")
    def _check_date_of_birth(self):
        age = self.count_employee_age()
        if age < ADULT:
            raise ValidationError("თანამშრომელი უნდა იყოს სრულწლოვანი")

    @api.constrains("date_of_issue")
    def _check_date_of_issue(self):
        for record in self:
            if record.date_of_issue > TODAY:
                raise ValidationError(
                    "პირადობის გაცემის თარიღი უნდა იყოს დღევანდელი დღე ან წინა დღეები"
                )

    @api.constrains("date_expiry")
    def _check_date_expiry(self):
        for record in self:
            if record.date_expiry < TODAY:
                raise ValidationError("პირად ნომერს ვადა აქვს გასული")

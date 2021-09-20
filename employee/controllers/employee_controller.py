from odoo import http
from odoo.http import request
import json


class EmployeeController(http.Controller):
    @http.route("/employee-list", author="public")
    def render_employee_list(self):
        employee_list_query = request.env["employee.employee"].search([])
        employee_list = []
        for employee in employee_list_query:
            values = {
                "first_name": employee.first_name,
                "last_name": employee.last_name,
            }
            employee_list.append(values)
        data = json.dumps(employee_list)
        return data

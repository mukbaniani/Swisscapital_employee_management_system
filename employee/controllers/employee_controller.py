from odoo import http
from odoo.http import request, Response
import json


class EmployeeController(http.Controller):
    @http.route("/employee-list", author="public")
    def render_employee_list(self):
        employee_list_query = (
            request.env["employee.employee"]
            .search([])
            .read(["first_name", "last_name", "citizenship"])
        )
        return Response(
            json.dumps(employee_list_query),
            content_type="application/json;charset=utf-8",
            status=200,
        )

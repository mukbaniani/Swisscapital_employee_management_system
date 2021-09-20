from odoo import models


class EmployeeReport(models.AbstractModel):
    _name = "report.employee.abstract_employee_id"
    _description = "SQL employee view"

    def _get_report_values(self, docids, data=None):
        docs = self.env["employee.employee"].browse(docids[0])
        return {
            "doc_model": "employee.employee",
            "data": data,
            "docs": docs,
        }

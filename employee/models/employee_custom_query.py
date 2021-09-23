from odoo import fields, models, tools, api


class EmployeeCustomView(models.AbstractModel):
    _name = "employee.view"
    _description = "employee SQL view"
    _auto = False

    first_name = fields.Char(string="სახელი")
    last_name = fields.Char(string="გვარი")
    person_number = fields.Char(string="პირადი ნომერი")
    department_id = fields.Many2one("department.department", string="დეპარტამენტი")

    def init(self):
        tools.drop_view_if_exists(self.env.cr, self._table)
        self.env.cr.execute(
            """CREATE or REPLACE VIEW %s as (
                           SELECT
                              emp.id AS id, emp.first_name, emp.last_name, emp.person_number, emp.department_id 
                           FROM
                              employee_employee AS emp
          )"""
            % self._table
        )

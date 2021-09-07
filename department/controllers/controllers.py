# -*- coding: utf-8 -*-
# from odoo import http


# class Department(http.Controller):
#     @http.route('/department/department/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/department/department/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('department.listing', {
#             'root': '/department/department',
#             'objects': http.request.env['department.department'].search([]),
#         })

#     @http.route('/department/department/objects/<model("department.department"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('department.object', {
#             'object': obj
#         })

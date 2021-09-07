# -*- coding: utf-8 -*-
# from odoo import http


# class PersonalQuality(http.Controller):
#     @http.route('/personal_quality/personal_quality/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/personal_quality/personal_quality/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('personal_quality.listing', {
#             'root': '/personal_quality/personal_quality',
#             'objects': http.request.env['personal_quality.personal_quality'].search([]),
#         })

#     @http.route('/personal_quality/personal_quality/objects/<model("personal_quality.personal_quality"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('personal_quality.object', {
#             'object': obj
#         })

# -*- coding: utf-8 -*-
# from odoo import http


# class Disfresses(http.Controller):
#     @http.route('/disfresses/disfresses', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/disfresses/disfresses/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('disfresses.listing', {
#             'root': '/disfresses/disfresses',
#             'objects': http.request.env['disfresses.disfresses'].search([]),
#         })

#     @http.route('/disfresses/disfresses/objects/<model("disfresses.disfresses"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('disfresses.object', {
#             'object': obj
#         })

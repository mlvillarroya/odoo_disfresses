from odoo import models, fields, api


class NoSaleOptions(models.Model):
    _name = 'no_sale_options'
    _description = 'What if the custome does not sell'

    name = fields.Char()

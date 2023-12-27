from odoo import models, fields, api


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    def _get_default_no_sale(self):
        value = None
        try:
            value = self.env.ref('disfresses.no_sale_option_1').id
        finally:
            return value

    no_sale_option_id = fields.Many2one(comodel_name='no_sale_options', string='Si no es ven', default=_get_default_no_sale)

    @api.model
    def default_get(self, fields):
        res = super(ProductTemplate, self).default_get(fields)
        res.update({
            'list_price': 5,
            'purchase_ok': False,
            'taxes_id': None,
            'detailed_type': 'product',
            'pos_categ_id': self.env.ref('disfresses.pos_category_disfressa').id,
        })
        return res






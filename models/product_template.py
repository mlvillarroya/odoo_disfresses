from odoo import models, fields, api


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    # no_sale_option = fields.Many2one(comodel_name='no_sale_options', string='Si no es ven', default=_get_default_no_sale)
    no_sale_option = fields.Selection(string="Si no es ven", selection=[
        ('DONATE', 'El vol donar'),
        ('RETRIEVE', 'El vol recuperar')],
        default='DONATE')

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






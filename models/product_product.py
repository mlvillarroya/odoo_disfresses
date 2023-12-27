from odoo import models, fields, api

class ProductProduct(models.Model):
    _inherit = 'product.product'

    @api.model
    def create(self, vals):
        result = super(ProductProduct, self).create(vals)
        location = self.env.ref('stock.stock_location_stock')
        self.env['stock.quant']._update_available_quantity(result, location, 1)
        if result.pos_categ_id.name == 'Disfressa':
            result.write({'default_code':  self.env['ir.sequence'].next_by_code('disfressa_sequence_code')})
        elif result.pos_categ_id.name == 'Perruca':
            result.write({'default_code':  self.env['ir.sequence'].next_by_code('perruca_sequence_code')})
        elif result.pos_categ_id.name == 'Accesori':
            result.write({'default_code':  self.env['ir.sequence'].next_by_code('accesori_sequence_code')})
        else:
            result.write({'default_code':  self.env['ir.sequence'].next_by_code('altres_sequence_code')})
        return result
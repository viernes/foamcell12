from odoo import api, fields, models, _

class SaleSignature(models.Model):
    _inherit = 'res.users'

    signatureSale = fields.Html(string='Firma ventas')

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    product_kit = fields.One2many(comodel_name="mrp.bom", inverse_name="product_tmpl_id", string="Kit")


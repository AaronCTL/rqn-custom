# -*- coding: utf-8 -*-
# Copyright 2016 Rooms For (Hong Kong) Limited T/A OSCG
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models


class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    show_user = fields.Boolean(
        string="Show Salesperson",
    )
    doc_title = fields.Char(
        string="Doc Title",
    )

    @api.multi
    def _prepare_order(self):
        res = super(PurchaseOrder, self)._prepare_order()
        res.update({'doc_title': self.doc_title})
        return res

    user_id = fields.Many2one('res.users', string='Salesperson', track_visibility='onchange',default=lambda self: self.env.user)
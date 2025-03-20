# -*- coding: utf-8 -*-

from odoo import models, fields, api

class AccountMove(models.Model):
    _inherit = 'account.move'

    first_route_id = fields.Many2one(
        'stock.route',
        string='Route',
        compute='_compute_first_route',
        store=True,
        readonly=True,
    )

    @api.depends('invoice_line_ids.sale_line_ids', 'invoice_line_ids.sale_line_ids.route_id')
    def _compute_first_route(self):
        for move in self:
            route = False
            if move.move_type in ('out_invoice', 'out_refund'):
                for line in move.invoice_line_ids:
                    for sale_line in line.sale_line_ids:
                        if sale_line.route_id:
                            route = sale_line.route_id
                            break
                    if route:
                        break
            move.first_route_id = route 
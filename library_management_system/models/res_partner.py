# -*- coding: utf-8 -*-
from odoo import models, fields, api

class ResPartner(models.Model):
    _inherit = 'res.partner'

    is_library_member = fields.Boolean(string="Library Member")
    loan_ids = fields.One2many('library.loan', 'partner_id')
    loan_count = fields.Integer(compute='_compute_loan_count')

    @api.depends('loan_ids')
    def _compute_loan_count(self):
        for partner in self:
            partner.loan_count = len(partner.loan_ids.filtered(lambda l: l.status == 'active'))

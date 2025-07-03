# -*- coding: utf-8 -*-
from datetime import date, timedelta

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class LibraryLoan(models.Model):
    _name = 'library.loan'
    _description = 'Library Loan'
    _rec_name = 'loan_number'

    loan_number = fields.Char(string="Loan Number")
    book_id = fields.Many2one('library.book', required=True)
    partner_id = fields.Many2one('res.partner', required=True)
    borrow_date = fields.Date(default=fields.Date.today)
    return_date = fields.Date()
    status = fields.Selection([
        ('draft', 'Draft'),
        ('borrowed', 'Borrowed'),
        ('returned', 'Returned'),
        ('overdue', 'Overdue')
    ], default='draft', tracking=True)

    # @api.constrains('book_id')
    # def _check_book_availability(self):
    #     for record in self:
    #         if record.book_id.status == 'borrowed':
    #             raise ValidationError("Book is already borrowed.")
    #
    # @api.model
    # def create(self, vals):
    #     res = super().create(vals)
    #     book = self.env['library.book'].browse(vals['book_id'])
    #     book.status = 'borrowed'
    #     return res
    #
    # def write(self, vals):
    #     res = super().write(vals)
    #     for record in self:
    #         if record.status == 'returned':
    #             record.book_id.status = 'available'
    #     return res

    def action_borrow(self):
        for record in self:
            if record.book_id.status == 'borrowed':
                raise ValidationError("Book is already borrowed.")
            record.status = 'borrowed'
            record.book_id.status = 'borrowed'

    def action_return(self):
        for record in self:
            record.status = 'returned'
            record.book_id.status = 'available'

    def action_mark_overdue(self):
        for record in self:
            if record.status == 'borrowed' and record.return_date and record.return_date < date.today() - timedelta(
                    days=14):
                record.status = 'overdue'

    @api.model
    def check_overdue_loans(self):
        overdue_loans = self.search([
            ('status', '=', 'borrowed'),
            ('return_date', '<', date.today() - timedelta(days=14))
        ])
        overdue_loans.action_mark_overdue()

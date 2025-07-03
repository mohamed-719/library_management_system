# -*- coding: utf-8 -*-
from odoo import api, fields, models
from odoo.exceptions import ValidationError


class LibraryBook(models.Model):
    _name = 'library.book'
    _description = 'Library Book'
    _rec_name = 'title'

    title = fields.Char(required=True)
    author = fields.Char(required=True)
    isbn = fields.Char(string="ISBN", required=True)
    publication_year = fields.Integer()
    status = fields.Selection([
        ('available', 'Available'),
        ('borrowed', 'Borrowed')
    ], default='available')


    @api.constrains('isbn')
    def _check_isbn_length(self):
        for record in self:
            if len(record.isbn) != 13 or not record.isbn.isdigit():
                raise ValidationError("ISBN must be exactly 13 digits.")
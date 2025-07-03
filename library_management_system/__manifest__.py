# -*- coding: utf-8 -*-
{
    'name': 'Library Management System',
    'version': '1.0',
    'summary': 'Manage books and loans in a library',
    'description': '''
        Manage books and loans in a library
    ''',
    'author': 'Mohamed Fathi',
    'website': 'https://www.cybrosys.com',
    'depends': ['base'],
    'data': [
        "security/ir.model.access.csv",
        "security/library_security.xml",
        "views/library_book_views.xml",
        "views/library_loan_views.xml",
        "views/res_partner_views.xml",
        "reports/library_loan_report.xml",
        "reports/report_templates.xml",
        "views/library_menu.xml",
        "data/cron_overdue_loans.xml"

    ],
    'license': 'LGPL-3',
    'installable': True,
    'application': False,
    'auto_install': False,
}

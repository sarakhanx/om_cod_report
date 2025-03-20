{
    'name': 'Invoice List Report',
    'version': '17.0.1.0.0',
    'category': 'Accounting',
    'summary': 'Custom Invoice List Report with Additional Fields',
    'description': """
        This module adds a custom report action to print selected invoices from list view with additional information:
        * Referenced Sale Order
        * Payment Status
        * Journal Name
        * Salesperson
        * Route
    """,
    'depends': ['account', 'sale', 'stock', 'sale_stock'],
    'data': [
        'security/ir.model.access.csv',
        'views/account_move_views.xml',
        'reports/invoice_list_report.xml',
        'reports/invoice_list_template.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
    'license': 'LGPL-3',
} 
{
    'name': 'COD List Report',
    'version': '17.0.1.0.0',
    'category': 'Accounting',
    'summary': 'Custom COD List Report with Additional Fields',
    'description': """
        This module adds a custom report action to print selected COD from list view with additional information:
        * Referenced Sale Order
        * Payment Status
        * Journal Name
        * Salesperson
    """,
    'depends': ['account', 'sale'],
    'data': [
        'security/ir.model.access.csv',
        'reports/invoice_list_report.xml',
        'reports/invoice_list_template.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
    'license': 'LGPL-3',
} 
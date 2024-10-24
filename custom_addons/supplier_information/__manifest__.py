{
    'name': "YENA Supplier Information",
    'version': '1.0',
    'summary': "Adds supplier-related fields to res.partner",
    'author': "Emre MATARACI",
    'website': "https://yenaengineering.nl",
    'category': 'Inventory',
    'license': 'LGPL-3',
    'depends': ['base', 'contact_status'],
    'data': [
        'views/supplier_information.xml',
        'security/ir.model.access.csv',
    ],
    'installable': True,
    'auto_install': False,
}

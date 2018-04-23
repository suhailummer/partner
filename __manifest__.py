{
'name' : 'PARTNER MANAGEMENT',
    'version' : '1.1',
    'summary': 'Send Invoices and Track Payments',
    'sequence': 30,
    'description': """sales management system    """,
    'category': 'Accounting',
    'website': 'https://www.netexsystems.com/',
    'depends' : ['base','sale'],
    'data': [
                'views/partner.xml',
                'views/customer.xml',
                

        
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
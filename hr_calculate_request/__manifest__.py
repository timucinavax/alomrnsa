# -*- coding: utf-8 -*-
{
    'name': "Hr Calculate Request",
    'version': '16.0.1',
    'summary': 'Hr Calculate Request',
    'sequence': 12,
    'description': """Hr Calculate Request""",
    'category': 'Accounting',
    'author': "hamdanerp",
    'maintainer': 'hamdanerp',
    'website': "https://www.hamdanerp.com",
    'license': 'AGPL-3',
    'depends': ['base', 'hr','hr_contract','hr_payroll'],
    'data': [
        'views/hr_contract.xml',
    ],
    'demo': [],
    'qweb': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}

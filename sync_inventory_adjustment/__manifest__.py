# -*- coding: utf-8 -*-
# Part of Odoo. See COPYRIGHT & LICENSE files for full copyright and licensing details.

{
    'name': 'Inventory Adjustment Screen',
    'version': '16.0.2',
    'category': 'Project',
    'author': 'Synconics Technologies Pvt. Ltd.',
    'summary': '',
    'website': 'www.synconics.com',
    'description': """
        Inventory Adjustment Screen
""",
    'depends': ['stock', "sb_one2many_search_widget"],
    'data': [
        'security/ir.model.access.csv',
        'views/stock_inventory_view.xml',
        'reports/report_stock_inventory.xml',
        'views/adj_inv_sequence.xml',
    ],
    'images': [
        'static/description/main_screen.png'
    ],
    'demo': [],
    'price': 35.0,
    'currency': 'USD',
    'application': True,
    'installable': True,
    'auto_install': False,
    'license': 'OPL-1',
}

# -*- coding: utf-8 -*-
{
    'name': "Monto en letras - Reporte Facturas",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Modulo para convertir el Total a Letras
    """,

    'author': "PromitGT",
    'website': "https://www.promitgt.com/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

 'depends': [
        'base',
        'account',
        'report',
    ],

     'data': [
        'views/res_currency_view.xml',
        'views/report_invoice.xml',
    ],
}

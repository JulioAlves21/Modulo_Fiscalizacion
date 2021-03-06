# -*- coding: utf-8 -*-
{
    'name': "ATM Inspection",

    'summary': """
        Modulo correspondiente a sector Fiscalizacion ATM  """,

    'description': """
        Long description of module's purpose
    """,

    'author': "Julio Alves",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['hr','account'],

    # always loaded
    'data': [
        'views/res_partner_inherit_view.xml',
        'views/inspection_views.xml',
        'views/expedient_views.xml',
        'views/hr_employee_inherit_view.xml',
        'views/inspection_user_view.xml',
        'security/security.xml',
        'security/ir.model.access.csv',
    ],

}


# -*- coding: utf-8 -*-
{
    'name': "custom_login",
    'summary': "custom login page",
    'description': """
    This is mmodule is teach me on how to make a custom login page theme
    """,

    'author': "Bisyri",
    'website': "https://github.com/Bisyri07/Odoo17_part2",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '17.0.1.0.0',

    'application':True,
    'installable':True,
    'auth_install': False,
    'license':'LGPL-3',

    # any module necessary for this one to work correctly
    'depends': ['base', 'auth_signup', 'web'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'assets': {
        "web.assets_frontend": [
            ('include', 'web._assets_bootstrap_frontend'),
            "backend_theme_explorer/static/fonts/poppins.css",
            "backend_theme_explorer/static/src/scss/login.scss",
        ],
    }
}


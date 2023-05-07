# -*- coding: utf-8 -*-
{
    'name': "epark",

    'summary': """
        Sistema para estacionamientos by elitesystems""",

    'description': """
        Registro de autos, clientes
        entradas y salidas
        cobros
        impresión de tickets,
        tickets extraviados
    """,

    'author': "Jose M Martz",
    'website': "https://www.opentechmx.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/flectra/flectra/blob/master/flectra/addons/base/module/module_data.xml
    # for the full list
    'category': 'Parking',
    'version': '0.6',

    # any module necessary for this one to work correctly
    'depends': ['base','mail'],

    # always loaded
    'data': [
        'views/ticket_view.xml',
        'views/caja_view.xml',
        'views/pension_view.xml',
        'views/tarifas_view.xml',
        'report/ticket_report.xml',
        'data/menu.xml',
        'data/sequence.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
# -*- coding: utf-8 -*-
# Copyright 2014 Graeme Gellatly
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Sale Partcode Replacement',
    'version': '10.0.1.0.0',
    'license': 'AGPL-3',
    'category': 'Sales & Purchases',
    'summary': 'Allows all products of a sale order to be updated by '
               'substituting part of their partcode',
    'author': 'O4SB - Graeme Gellatly',
    'website': 'https://o4sb.com',
    'depends': ['sale'],
    'data': [
        'wizard/sale_partcode_replacement.xml'
    ],
    'installable': True,
}

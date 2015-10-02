#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2010 Doug Hellmann.  All rights reserved.
#
"""
"""
#end_pymotw_header

import locale

sample_locales = [ ('USA',      'en_US'),
                   ('Argentina','es_AR'),
                   ('Spain',    'es_ES'),
                   ('Brazil',   'pt_BR'),
                   ('Mexico',   'es_MX'),
                   ]

print '%20s %15s %20s' % ('Locale', 'Integer', 'Float')
for name, loc in sample_locales:
    locale.setlocale(locale.LC_ALL, loc)

    print '%20s' % name,
    print locale.format('%15d', 123456, grouping=True),
    print locale.format('%20.2f', 123456.78, grouping=True)

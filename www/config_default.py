#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Default configurations.
'''

__author__ = 'Michael Liao'

configs = {
    'debug': True,
    'db': {
        'host': '172.18.108.118',
        'port': 3306,
        'user': 'root',
        'password': '1234',
        'db': 'awesome'
    },
    'session': {
        'secret': 'Awesome'
    }
}

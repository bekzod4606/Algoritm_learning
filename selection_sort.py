# -*- coding: utf-8 -*-
"""
Created on Wed Feb 15 17:02:44 2023

@author: bekzo
"""
import operator
narx = {
        'Tahoe':66000,
        'Nexia':10000,
        'Damas':9000,
        'Gentra':15000,
        'Cobalt':13000
        }
saralangan = {}
for key, value in sorted(narx.items(), key=operator.itemgetter(1)):
    saralangan[key] = value
    print(saralangan)
        
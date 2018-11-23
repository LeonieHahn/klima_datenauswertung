# -*- coding: utf-8 -*-
"""
Created on Thu Nov 22 20:07:42 2018

@author: kgn
"""

class Measurement():
    
    def __init__(self, id, datum, temp_1, water_1, temp_2, water_2):
        self.id = id
        self.datum = datum
        self.temp_1 = temp_1
        self.water_1 = water_1
        self.temp_2 = temp_2
        self.water_2 = water_2

#!/usr/bin/env python3 
#  -*- coding: utf-8 -*-
print(list(map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9])))

def build(x, y):
    return lambda: x * x + y * y


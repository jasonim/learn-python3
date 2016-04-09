#!/usr/bin/env python3
# -*- coding: utf-8 -*-


mylist = [x*x for x in range(1, 11) if x % 2 == 0]
print(mylist)

d = {'x': 'A', 'y': 'B', 'z': 'C' }
print([k + '=' + v for k, v in d.items()])
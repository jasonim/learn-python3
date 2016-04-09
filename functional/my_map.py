#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from functools import reduce

print(list(map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9])))


def add(x, y):
    return x + y


print(reduce(add, [1, 3, 5, 7, 9]))

# print({'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}['12578'])


def str2int(s):
    def fn(x, y):
        return x * 10 + y

    def char2num(s):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]

    return reduce(fn, map(char2num, s))
print(str2int('12578'))

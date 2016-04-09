#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def power(x, n=2):
    s = 1
    while n > 0:
        n -= 1
        s = s * x
    return s


def add_end(L=None):
    if L is None:
        L = []
    L.append('END')
    return L


# var args
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

nums = [1, 2, 3]
print(calc(*nums))
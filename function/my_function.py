#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# define
import math


def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x


def nopass():
    pass


# check parameter
def my_abs_check(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x


# return many object
def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny


print(move(5, 7, 1))

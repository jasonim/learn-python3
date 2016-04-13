#!/usr/bin/env python 
#  -*- coding: utf-8 -*-
import functools

int2 = functools.partial(int, base=2)

print(int2('1000011'))

max2 = functools.partial(max, 10)

print(max2(5, 6, 7))


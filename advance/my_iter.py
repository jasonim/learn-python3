#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from collections import Iterable
from typing import Iterator

d = {'a': 1, 'b': 2, 'c': 3}
for k, v in d.items():
    print(k, v)
print(isinstance('abc', Iterable))
print(isinstance(d, Iterable))
print(isinstance(123, Iterable))

for x, y in [(1, 1), (2, 4), (3, 9)]:
    print(x, y)

print(isinstance('abc', Iterator))
print(isinstance(d, Iterator))
print(isinstance((x for x in range(10)), Iterator))
print(isinstance(iter(d), Iterator))

# 首先获得Iterator对象:
it = iter([1, 2, 3, 4, 5])
# 循环:
while True:
    try:
        # 获得下一个值:
        x = next(it)
    except StopIteration:
        # 遇到StopIteration就退出循环
        break
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
for n in (x * x for x in range(10)):
    print(n)
g = (x * x for x in range(10))

print(g)
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n += 1
    return 'done'
print(fib(5))
for n in fib(5):
    print(n)
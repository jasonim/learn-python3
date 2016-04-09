#!/usr/bin/env python3 
#  -*- coding: utf-8 -*-

def _odd_iter():
    n = 1
    while True:
        n += 2
        yield n


def _not_divisible(n):
    return lambda x: x % n > 0


def primes():
    yield 2
    it = _odd_iter()  # 初始序列
    while True:
        n = next(it)  # 返回序列的第一个数
        # for i in it:
        #     if i <= n:
        #         print("in", i)
        #     else:
        #         print("esle", i)
        #         break
        yield n
        # print(1)
        it = filter(_not_divisible(n), it)  # 构造新序列

for n in primes():
    if n < 10:
        print(n)
    else:
        break

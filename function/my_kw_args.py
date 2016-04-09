#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)

person('Bob', 35, city='Beijing')
extra = {'city': 'Beijing', 'job': 'Engineer'}
person('Jack', 24, **extra)

def person_name(name, age, *, city='Beijing'):
    print(name, age, city)
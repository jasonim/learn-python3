#!/usr/bin/env python3

# -*- coding: utf-8 -*-



class Animal(object):
    name = "animal"
    def __init__(self, name):
        self.name = name
    def run(self):

        print('Animal is running...')




animal = Animal('xiaoqiang')
print(hasattr(animal, 'name'))
print(hasattr(animal, 'run'))

print(animal.name)
print(Animal.name)

animal.name = 'xiaoha'
print(animal.name)

del animal.name

print(Animal.name)

print(animal.name)



#!/usr/bin/env python3
# -*- coding: utf-8 -*-
people = ['Jason', 'xiaoming', 'Bob']
print people, len(people)

print people[-1]
# print people[-4] out of range
people.insert(1, 'Jack')

print(people)
print people.pop()

s = ['python', 'java', people, 'c']
print s

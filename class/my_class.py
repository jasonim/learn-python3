#!/usr/bin/env python 
#  -*- coding: utf-8 -*-

class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print('%s: %s' % (self.name, self.score))

stu = Student('jason', '7')
print(stu.name, stu.score)
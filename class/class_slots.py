#!/usr/bin/env python 
#  -*- coding: utf-8 -*-
from types import MethodType


class Student(object):
    __slots__ = ('name', 'age') # 用tuple定义允许绑定的属性名称
    pass

def set_age(self, age): # 定义一个函数作为实例方法
    self.age = age


s = Student()
s.set_age = MethodType(set_age, s) # 给实例绑定一个方法
s.set_age(20)
print(s.age)
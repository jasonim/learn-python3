#!/usr/bin/env python3

# -*- coding: utf-8 -*-
import os

path = os.path.abspath('.')

print(path)

join_path = os.path.join(path, 'testdir')
os.mkdir(join_path)

os.rmdir(join_path)

print(os.path.split(join_path + "file.log"))
print(os.path.splitext(join_path + "file.log"))

print([x for x in os.listdir('.') if os.path.isdir(x)])

print(os.listdir('.'))

print([x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py'])
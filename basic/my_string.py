#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# string encode decode
s = '中文'
print(s, len(s))
print(isinstance('中文', str))
print(isinstance(u'中文', str))
b = u'中文'.encode(encoding='utf8')
print(b)
print(s.decode('utf-8'))

# string reformat
print('hello, %s' % 'world')
print('%2d-%02d %.2f' % (3, 1, 3.1415926))
print('age: %s jason:%s' % (25, True))
print('growth rate: %d %%' % 7)

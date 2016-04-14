#!/usr/bin/env python3

# -*- coding: utf-8 -*-
from io import StringIO

f = StringIO()

print(f.write('hello'))

print(f.getvalue())
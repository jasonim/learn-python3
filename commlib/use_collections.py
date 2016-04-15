#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from collections import namedtuple
from collections import deque
from collections import defaultdict
from collections import OrderedDict


Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
print(p.x, p.y)

q = deque(['a', 'b', 'c'])
q.append('x')
q.appendleft('y')

dd = defaultdict(lambda: 'N/A')
dd['key1'] = 'abc'
print(dd['key1'], dd['key3'])

od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
print(od)


class LastUpdatedOrderedDict(OrderedDict):

    def __init__(self, capacity):
        super(LastUpdatedOrderedDict, self).__init__()
        self._capacity = capacity

    def __setitem__(self, key, value):
        containsKey = 1 if key in self else 0
        if len(self) - containsKey >= self._capacity:
            last = self.popitem(last=False)
            print('remove:', last)
        if containsKey:
            del self[key]
            print('set:', (key, value))
        else:
            print('add:', (key, value))
        OrderedDict.__setitem__(self, key, value)

from collections import Counter
c = Counter()
for ch in 'programming':
    c[ch] = c[ch] + 1
print(c)
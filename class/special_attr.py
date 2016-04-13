#!/usr/bin/env python
#  # -*- coding: utf-8 -*-


class Chain(object):

    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):
        print(path)
        return Chain('%s/%s' % (self._path, path))

    def __str__(self):
        return self._path

    __repr__ = __str__

    def users(self, name):
        self.__name = name
        return Chain('%s/%s' % (self._path, self.__name))
print(Chain().status.user.timeline.list)
print(Chain().users('jason').repos)
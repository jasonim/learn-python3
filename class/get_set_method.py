#!/usr/bin/env python
#  # -*- coding: utf-8 -*-

class Student(object):

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value

s = Student()
s.score = 100
# s.score = 10000

class Screen(object):

    @property
    def width(self):
        return self.__width
    @width.setter
    def width(self, v):
        self.__width = v

    @property
    def height(self):
        return self.__height
    @height.setter
    def height(self, v):
        self.__height = v

    @property
    def resolution(self) :
        #self._width * self._height is ok
        return self.width * self.__height

screen = Screen()
screen.width = 1
screen.height = 2

print(screen.resolution)
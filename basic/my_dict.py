#!/usr/bin/env python3
# -*- coding: utf-8 -*-
people = {'Jason': 20, 'xiaoming': 19, 'Bob': 35}

if 'Jason' in people:
    print(people['Jason'])

people.get('jack', -1)

people.pop('Bob')

# key is not change
key = [1, 2, 3]
people[key] = 'a list'
# error



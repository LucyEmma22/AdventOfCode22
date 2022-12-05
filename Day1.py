#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  4 10:43:23 2022

@author: s1995754
"""

with open("calories.txt", 'r') as cals:
    cals = list([x.replace('\n', '') for x in cals])
    cals.append('')
    backpack=list()
    count=0
    for line in cals:
        if line!='':
            count = count + float(line)
        else:
            backpack.append(count)
            count=0

sum(sorted(backpack,reverse=True)[0:3])

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  6 10:50:33 2022

@author: s1995754
"""

with open('communications.txt','r') as communications:
    communications = communications.read().replace('\n', '')

padding = str()
for letter in communications:
    padding = padding + letter
    if (len(set(padding[-4:])) == len(padding[-4:])) & (len(set(padding[-4:]))==4):
        break
len(padding)
        
padding = str()
for letter in communications:
    padding = padding + letter
    if (len(set(padding[-14:])) == len(padding[-14:])) & (len(set(padding[-14:]))==14):
        break
len(padding)
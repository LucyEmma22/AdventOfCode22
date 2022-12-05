#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 11:11:41 2022

@author: s1995754
"""
import re
with open('cleaning_pairs.txt','r') as cp:
    full_contain=list()
    count=0
    for line in cp:
        x = list(map(int,re.findall('(\d+)',line.strip())))
        if(((x[0] <= x[2]) & (x[1] >= x[3])) or ((x[0] >= x[2]) & (x[1] <= x[3]))):
            full_contain.append(line.strip())
            count=count+1
        else:
            count=count


with open('cleaning_pairs.txt','r') as cp:
    no_contain=list()
    count=0
    for line in cp:
        x = list(map(int,re.findall('(\d+)',line.strip())))
        #if(((x[0] < x[2]) & (x[1] < x[2])) or ((x[3] < x[1]) & (x[2] > x[1]))):
        if((x[1] < x[2]) or (x[3] < x[0])):

            count=count
            no_contain.append(line.strip())
        else:
            count=count+1
            
         
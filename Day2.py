#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  4 11:58:31 2022

@author: s1995754
"""
import pandas as pd

rps = pd.read_csv('rock_paper_scissors.txt', sep=" ", header=None)
rps.columns = ["opponent", "me"]

key = pd.DataFrame({'opponent': ['A', 'A', 'A', 'B', 'B', 'B', 'C', 'C', 'C'],
                    'me': ['X', 'Y', 'Z', 'X', 'Y', 'Z', 'X', 'Y', 'Z'],
                    'score':[3+1, 6+2, 0+3, 0+1, 3+2, 6+3, 6+1, 0+2, 3+3]})
rps2 = pd.merge(rps, key, on=['opponent','me'],how='left')
rps2['score'].sum()


key2 = pd.DataFrame({'opponent': ['A', 'A', 'A', 'B', 'B', 'B', 'C', 'C', 'C'],
                    'me': ['X', 'Y', 'Z', 'X', 'Y', 'Z', 'X', 'Y', 'Z'],
                    'score':[0+3, 3+1, 6+2, 0+1, 3+2, 6+3, 0+2, 3+3, 6+1]})
rps3 = pd.merge(rps, key2, on=['opponent','me'],how='left')
rps3['score'].sum()






# A rock      X rock      draw - draw 3 
# A rock      Y paper     paper - win 6
# A rock      Z scissors  rock - lose 0
# B paper     X rock      paper - lose 0
# B paper     Y paper     draw - draw 3
# B paper     Z scissors  scissors - win 6
# C scissors  X rock      rock - win 6
# C scissors  Y paper     scissors - lose 0
# C scissors  Z scissors  draw - draw 3


# A rock      X lose 0     scissors 3 
# A rock      Y draw 3     rock 1 
# A rock      Z win  6     paper 2 
# B paper     X lose 0     rock 1 
# B paper     Y draw 3     paper 2 
# B paper     Z win  6     scissors 3 
# C scissors  X lose 0     paper 2
# C scissors  Y draw 3     scissors 3
# C scissors  Z win  6     rock 1

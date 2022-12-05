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

import re
crates = [['J', 'H', 'G', 'M', 'Z', 'N', 'T', 'F'],
          ['V', 'W', 'J'],
          ['G', 'V', 'L', 'J', 'B', 'T', 'H'],
          ['B', 'P', 'J', 'N', 'C', 'D', 'V', 'L'],
          ['F', 'W', 'S', 'M', 'P', 'R', 'G'],
          ['G', 'H', 'C', 'F', 'B', 'N', 'V', 'M'],
          ['D', 'H', 'G', 'M', 'R'],
          ['H', 'N', 'M', 'V', 'Z', 'D'],
          ['G', 'N', 'F', 'H']]

with open ('crates.txt') as instructions:
    for _ in range(10):
        next(instructions)
    for line in instructions:
        x = list(map(int,re.findall('(\d+)',line.strip())))
        for i in range (x[0]):
            crates[x[2]-1].append(crates[x[1]-1][-1])
            del crates[x[1]-1][-1]        
new_list = [crate[-1] for crate in crates]


with open ('crates.txt') as instructions:
    for _ in range(10):
        next(instructions)
    for line in instructions:
        x = list(map(int,re.findall('(\d+)',line.strip())))
        crates[x[2]-1] = crates[x[2]-1] + crates[x[1]-1][-x[0]:]
        del crates[x[1]-1][-x[0]:]
            
new_list = [crate[-1] for crate in crates]

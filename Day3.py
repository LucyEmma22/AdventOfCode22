with open('item_type.txt','r') as items:
    baglist=list()
    for line in items:
        firsthalf, secondhalf = (line[:len(line)//2]), (line[len(line)//2:])
        common = str(set(firsthalf).intersection(secondhalf))
        if common[2].upper() == common[2]:
            common = ord(common[2]) - 38
        else:
            common = ord(common[2]) - 96
        baglist.append(common)
sum(baglist)
            
    
with open('badges.txt','r') as badges:
    badgelist=list()
    counter=0
    for line in badges:
        if counter % 3 == 0:
            x = line.strip()
            counter=counter+1
        elif (counter-1) % 3==0:
            x = str(set(x).intersection(line.strip()))
            counter=counter+1
        elif (counter-2) % 3==0:
            x = str(set(x).intersection(line.strip()))
            if x[2].upper() == x[2]:
                common = ord(x[2]) - 38
            else:
                common = ord(x[2]) - 96
            badgelist.append(common)
            counter = counter + 1
sum(badgelist)

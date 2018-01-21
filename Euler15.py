a=[[0]*20 for x in range(0,20)]
a.append([1]*20)
for x in range(0,20):
    a[x].append(1)
for x in range(19,-1,-1):
    for y in range(19,-1,-1):
        a[x][y]=int(a[x+1][y])+int(a[x][y+1])
print(a)

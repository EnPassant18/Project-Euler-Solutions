f=open('number.txt')
c = f.readlines()
for x in range(0, len(c)):
    c[x]=int(c[x])
print(sum(c))


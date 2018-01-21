f=open('names.txt')
names=str(f.read())
names=names.split(',')
names.sort()
grand=0
for test in range(0,len(names)):
    total=0
    names[test]=names[test].strip('""')
    for x in range(0,len(names[test])):
        total+=ord(names[test][x])-64
    grand+=total*(test+1)
print(grand)

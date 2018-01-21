f=open('number.txt')
triangle=f.readlines()
for x in range(0, len(triangle)):
    triangle[x]=triangle[x].split(' ')
    for y in range(0, len(triangle[x])):
        triangle[x][y]=int(triangle[x][y])
y=0
for row in range(len(triangle)-2,-1,-1):
    for col in range(0,len(triangle[row])):
        triangle[row][col]+=max(triangle[row+1][col],triangle[row+1][col+1])
print(triangle[0][0])

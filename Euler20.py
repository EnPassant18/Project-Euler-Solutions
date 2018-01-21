y=1
for x in range(100,1,-1):
    y=y*x
z=0
while y:
    z=z+(y%10)
    y=y//10
print(z)

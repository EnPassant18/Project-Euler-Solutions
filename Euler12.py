import math
x=0
y=0
a=0
while a<250:
    a=0
    y=y+1
    x=x+y
    for z in range(1,int(math.sqrt(x))):
        if not(x%z):
            a=a+1
print(x)
            

import math
def prime(x):
    for a in range(3,int(math.sqrt(x))+1,2):
        if x%a==0:
           return False
    return True
b=2
for x in range(3,1999999,2):
    if prime(x):
        b=b+x
print(b) 


import math
def factorsum(x):
    total=1
    for y in range(2,int(math.sqrt(x))+1):
        if not(x%y):
            total+=y
            if not(x/y==y):
                total+=x/y
    return total
total=0
for test in range(3,10001):
    if factorsum(factorsum(test))==test and not(factorsum(test)==test):
        total+=test
print(total)

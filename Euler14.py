z=0
y=0
for x in range(999999,0,-1):
    a=x
    y=1
    while x>1:
        if not(x%2):
            x=x/2
        else:
            x=3*x+1
        y=y+1
    if y>z:
        z=y
        print(a)

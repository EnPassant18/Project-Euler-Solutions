a=0
for num in range(1,1000):
    s=0
    t=num%10	
    if t>0:
        if t==1 or t==2 or t==6:
            s=3
        elif t==4 or t==5 or t==9:
            s=4
        else:
            s=5
    t=num//10
    t=t%10
    if t>0:
        if t==1:
            t=num%10
            if t==1 or t==2:
                s=6
            elif t==3 or t==4 or t==8 or t==9:
                s=8
            elif t==5 or t==6:
                s=7
            elif t==7:
                s=9
            else:
                s=3
        elif t==2 or t==3 or t==4 or t==8 or t==9:
            s=s+6
        elif t==5 or t==6:
            s=s+5
        else:
            s=s+7
    t=num//100
    t=t%10
    if t>0:
        s=s+7
        if t==1 or t==2 or t==6:
            s=s+3
        elif t==4 or t==5 or t==9:
            s=s+4
        else:
            s=s+5
        if num%100>0:
            s=s+3
    if num==1000:
        s=11
    a=a+s
print(a)		

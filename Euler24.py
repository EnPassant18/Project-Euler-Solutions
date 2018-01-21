x=0
for a in range(10):
    for b in range(10):
        print(b)
        for c in range(10):
            for d in range(10):
                  for e in range(10):
                    for f in range(10):
                            for g in range(10):
                                for h in range(10):
                                    for i in range(10):
                                        if a!=b!=c!=d!=e!=f!=g!=h!=i:
                                            x+=1
                                            if x==1000000:
                                                break
print(str(a)+str(b)+str(c)+str(d)+str(e)+str(f)+str(g)+str(h)+str(i))

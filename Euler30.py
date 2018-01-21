grandtotal=0
for num in range(2,999999):
    total=0
    test=num
    for x in range(0,6):
        total+=(test%10)**5
        test//=10
    if total==num:
        grandtotal+=num
        print(num)
print(grandtotal)
        
    

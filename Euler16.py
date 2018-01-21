a=2**1000
b=0
while a:
    b=(a%10)+b
    a=a//10
print(b)

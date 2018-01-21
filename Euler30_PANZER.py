grandtotal = 0
for num in range(2, 999999):
    total = 0
    numString = str(num)
    for i in range(len(numString)):
        digit = int(numString[i])
        total = total + (digit**5)
    if total == num:
        grandtotal += num
        print(num)

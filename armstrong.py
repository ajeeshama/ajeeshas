
 sum = 0
 Temp = num
 While temp > 0:
    digit = temp % 10
    sum += digit ** 3
    Temp //= 10
 if num == sum:
    print(num,"is an Armstrong number")
 Else:
    print(num,"is not an Armstrong number")

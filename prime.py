  Number = int(input("Enter any Number: "))

  # prime Number is always greater than 1
        if Number > 1:
    for i in range(2, Number):
        if (Number % i) == 0:
             print(Number, "is not a prime Number")
            break
        else:
             print(Number, "is a prime Number")

# if the entered Number is less than or equal to 1
# then it is not prime Number
       else:
             print(Number, "is not a prime Number")

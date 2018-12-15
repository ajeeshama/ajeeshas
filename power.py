    Base, exponent = input("Enter Base and exponent : ").split()

    Base, exponent = [int(Base), int(exponent)]

    power = 1

        for i in range(1, exponent + 1):
    power = power * Base

 print("\nResult", Base, "^", exponent, ":", power)
 print("Using math class :", math.pow(Base, exponent))

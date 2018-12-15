 Num = input('Enter any Number : ')
 try:
       val = int(Num)
     if Num == str(Num)[::-1]:
          print('The given Number is PALINDROME')
     else:
          print('The given Number is NOT a palindrome')
 except ValueError:
         print("That's not a valid Number, Try Again !")

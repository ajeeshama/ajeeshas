 Lower = 900
 Upper = 1000
 Print("Prime numbers Between",Lower,"and",Upper,"are:")
  for num in range(Lower,Upper + 1):
    if num > 1:
        for i in range(2,num):
            if (num % i) == 0:
                break
        Else:
            Print(num)

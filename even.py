  Lower_limit = Int(Input("enter the lower limit : "))
  Upper_limit = Int(Input("enter the upper limit : "))
  for i in Range(lower_limit,upper_limit+1):
    if(i%2 == 0):
      print(i)

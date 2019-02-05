   Def sumofAP(a, n, d):
       total = (n * (2 * a + (n - 1) * d)) / 2
       return total

   a = int(input("Please Enter First Number of an A.P Series: : "))
   n = int(input("Please Enter the Total Numbers in this A.P Series: : "))
   d = int(input("Please Enter the Common Difference : "))

       total = sumofAP(a, n, d)
   Print("\nThe Sum of Arithmetic Progression Series = " , total)

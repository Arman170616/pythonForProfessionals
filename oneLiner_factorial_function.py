#general
Def fac(a):
   if a == 0 or a == 1:
       return 1
   else:
       return a*fac(a-1)
 
 print(fac(5))  
 

#using one-liner
 
 
import math
print(math.factorial(5))

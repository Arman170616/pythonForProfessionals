for i in range(0, 5):
 
   for j in range(0, i + 1):
       # printing stars
       print("* ", end="")
 
   # ending line after each row
   print("\r")
 
 
 
# one liner code for half pyramid pattern
n = 5
print('\n'.join('* ' * i for i in range(1, n + 1)))

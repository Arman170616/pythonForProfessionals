'''
A palindrome is a special word or number that, when read from the beginning of the end, 
does not change the pronunciation and meaning of the word or the value of the number remains the same.
'''

#general
n = input("Enter the word and see if it is palindrome: ")  # check palindrome
if n == n[::-1]:
   print(" palindrome")
else:
   print("not palindrome")
 
 
# One-Liner
def is_palindrome(phrase): return phrase == phrase[::-1]
print(is_palindrome("maam"))
print(is_palindrome("cat"))
print(is_palindrome("rats live on no evil star"))
'''
True
False
True
'''

x = 5
y = 10
# To take inputs from the user
#x = input('Enter value of x: ')
#y = input('Enter value of y: ')
 
# create a temporary variable and swap the values
temp = x
x = y
y = temp
 
print('The value of x after swapping: {}'.format(x))
print('The value of y after swapping: {}'.format(y))
 
# Python one-liner for swapping
 
x,y=10,5
print(x,y)
x,y=y,x
print(x,y)

'''
The right-hand side y, x is evaluated, that is to say, a tuple of two elements is created in the memory. 
The two elements are the objects designated by the identifiers y and x, that was existing before the instruction is 
encountered during the execution of the program.

Just after the creation of this tuple, no assignment of this tuple object has still been made,
but it doesn't matter, Python internally knows where it is.
Then, the left-hand side is evaluated, that is to say, the tuple is assigned to the left-hand side.
As the left-hand side is composed of two identifiers, the tuple is unpacked in order that the first
identifier a be assigned to the first element of the tuple (which is the object that was formerly y before 
the swap because it had name y)
and the second identifier y is assigned to the second element of the tuple (which is the object that was 
formerly x before the swap because its identifiers were x)

'''

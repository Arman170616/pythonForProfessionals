# Generate Random Password
from random import choice
print(''.join([choice('abcdefghijklmnopqrstuvwxyz0123456789%^*(-_=+)')
      for i in range(10)]))

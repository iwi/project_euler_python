#!/usr/bin/python

# Project Euler (projecteuler.net)
#
# Problem 1: Multiples of 3 and 5
#
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we
# get 3, 5, 6 and 9. The sum of these multiples is 23.
#
# Find the sum of all the multiples of 3 or 5 below 1000.

# to check divisibility
def is_divisible_by(n, divisor):
  if n % divisor == 0:
    return True
  else :
    return False 


# main calculation

# definition of the top limit
max_integer = 1000
big_sum = 0
for natural_number in xrange(1, max_integer) :
  if is_divisible_by(natural_number, 3) :
    big_sum += natural_number
    print natural_number
  elif is_divisible_by(natural_number, 5) :
    big_sum += natural_number
    print natural_number
  else:
    print '.'

# output
print big_sum
print 'The sum of all the multiples of 3 and/or 5 below ', max_integer, ' is ', big_sum        


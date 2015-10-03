#!/usr/bin/python
# Project Euler (projecteuler.net)
#
# Problem 5: Smallest multiple
#
# 2520 is the smallest number that can be divided by each of the numbers from
# 1 to 10 without any reminder
# What is the smallest positive number that is evenly divisible by all of the
# numbers from 1 to 20?


# this is probably too ineficient
# check if there is a better way
from p3_largest_prime_factor import is_prime

if __name__ == "__main__" :
  n = 2000000
  sumation = 0
  for test_number in xrange( 2, n + 1 ) :
    if is_prime( test_number ) :
      sumation += test_number

  print "The sum of all primes below", n, "is ", sumation


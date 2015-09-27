#!/usr/bin/python
# Project Euler (projecteuler.net)
#
# Problem 7: 100001st prime
#
# By listing the first six prime numbers: 2, 3, 5, 7, 11 and 13, we can see
# that the 6th prime is 13.
# What is the 10,001st prime number?

from p3_largest_prime_factor import is_prime

if __name__ == "__main__" :
  n = 10001
  print "n: ", n
  prime_counter = 0
  test_int = 1
  while prime_counter < n :
    test_int += 1
    if is_prime( test_int ) :
      prime_counter += 1
      print "The", prime_counter, "th prime number is ", test_int


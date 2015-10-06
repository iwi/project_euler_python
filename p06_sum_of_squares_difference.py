#!/usr/bin/python
# Project Euler (projecteuler.net)
#
# Problem 6: Sum square difference
#
# The sum of squares of the first ten natural numbers is, 
# 1^2 + 2^2 + ... + n^2 = 385
# The square sum of the first ten natural numbers is,
# (1 + 2 + ... + n)^2 = 3025
# Hence the difference between the sum of the squares of the first ten natural
# numbers and the square of the sum is 3025 - 385 = 2640.
# Find the difference between the sum of the squares of the first one hundred
# numbers and the square of the sum.


def sum_of_squares( n ) :
  sum_of_squares = n * ( n + 1 ) * ( 2 * n + 1 ) / 6
  print "sum of squares", ( sum_of_squares )
  return sum_of_squares 

def square_of_the_sum( n ) :
  sumation = ( 1 + n ) * n / 2
  square_of_the_sum = sumation * sumation
  print "square of the sum: ", square_of_the_sum 
  return square_of_the_sum 


if __name__ == "__main__" :
  n = 100  
  print "n: ", n
  difference = square_of_the_sum( n ) - sum_of_squares( n )
  print "difference: ", difference


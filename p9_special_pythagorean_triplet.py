#!/usr/bin/python                                                                     
# Project Euler (projecteuler.net)
#
# Problem 9: Special Pythagorean triplet
# 
# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
# a2 + b2 = c2
#
# For example, 32 + 42 = 9 + 16 = 25 = 52.
#
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.


# implementation of prime validation via regex is so slow that crashes!!
from math import sqrt 

def is_integer( n ) :
  return int( c ) == c

def is_pythagorean( x, y, z ) :
 return x**2 + y**2 == z**2

if __name__ == "__main__" :
  total = 1000
  for a in xrange( 3, total - 9 ) :
    for b in xrange( a + 1, total - 9 - a - 1 ) :
      c = sqrt( a**2 + b**2 )
      if is_integer( c ) and c == ( total - a - b ) :
        if is_pythagorean( a, b, c ) :
          c = int( c )
          product = a * b * c
          print 'a:', a
          print 'b:', b
          print 'c:', c
          print 'the product abc is', product


#!/usr/bin/python
# Project Euler (projecteuler.net)
#
# Problem 12: Highly divisible triangular number
# https://projecteuler.net/problem=12
#
#
# The sequence of triangle numbers is generated by adding the natural numbers.
# So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28.
# The first ten terms would be:
#
#    1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
#
# Let us list the factors of the first seven triangle numbers:
#
# 1: 1
# 3: 1,3
# 6: 1,2,3,6
# 10: 1,2,5,10
# 15: 1,3,5,15
# 21: 1,3,7,21
# 28: 1,2,4,7,14,28
#
# We can see that 28 is the first triangle number to have over five divisors.
#
# What is the value of the first triangle number to have over five hundred
# divisors?

import numpy as na
from math import sqrt
from p03_largest_prime_factor import is_factor

def count_factors( x ) :
    if x == 1 :
        counter = 0
    else :
        counter = 0 
        for element in xrange( 1, int( x / 2 ) + 1 ) :
            print element
            if is_factor( element, x ) :
                counter += 1
    return counter + 1  # The +1 is to count itself

def triangular_of( n ) :
    triangular_n = 0
    for counter in xrange( 1, n + 1 ) :
        triangular_n += counter 
    return triangular_n

if __name__ == "__main__" :
    min_number_of_divisors = 5 
    ith = 1 
    triangular_number = triangular_of( ith ) 
    factors_counter = count_factors( triangular_number )
    print "number of factors =", factors_counter
    while factors_counter < min_number_of_divisors :
        factors_counter = count_factors( triangular_number )
        ith += 1
        triangular_number += ith
        print "number of factors =", factors_counter
    print "The first triangular number with", min_number_of_divisors, "+ divisors is", triangular_number
    print "It has", factors_counter, "divisors"

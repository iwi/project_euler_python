#!/usr/bin/python
# Project Euler (projecteuler.net)
#
# Problem 4: Largest palindrome product
#
# A palindromic number reads the same both ways. the largest palindrome made from
# the product of two 2-digit numbers is 9009 = 91 x 99.
#
# Find the largest palidrome made from the product of thwo 3-digit numbers.


# check if a number is a palindrome
def is_pair ( n ) :
  return 0 == n % 2

# this is an attempt to use map and reduce even if it's not the optimal 
# algorithm to solve the problem
 
#def is_palindrome ( n ) :
#  n_as_string = str( n )
#  length_of_n = len( n_as_string )
#  if is_pair( n ) :
#    half_n = n / 2
#  else :
#    half_n = ( n - 1 ) / 2
#
#  palindrome = map( lambda s, half_n, i :
#    return s[ i ] == s[ half_n - i + 1 ]
#
#  return palindrome


def is_palindrome_2 ( n ) :
  n_as_string = str( n )
  return n_as_string[::-1] == n_as_string


if __name__ == "__main__" :
  factor_1 = 999
  factor_2 = 999
  match_sum = factor_1 + factor_2
  diagonal = 999 
   
  while factor_1 > 99 and factor_2 > 99 :
    num = factor_1 * factor_2
    print num
    if is_palindrome_2( num ) :
      print "the result is: ", num, " from ", factor_1, " times ", factor_2, " DONE!!!!"
      break
    elif factor_1 == 999 :
      if not(is_pair( factor_2 )) :
        factor_1 = diagonal - 1
        factor_2 = factor_1
        diagonal = factor_1
      else :
        factor_1 = diagonal
        factor_2 = diagonal - 1 
    else :
      factor_2 -= 1
      factor_1 += 1 

        

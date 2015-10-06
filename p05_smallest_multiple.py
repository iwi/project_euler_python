#!/usr/bin/python
# Project Euler (projecteuler.net)
#
# Problem 5: Smallest multiple
#
# 2520 is the smallest number that can be divided by each of the numbers from
# 1 to 10 without any reminder
# What is the smallest positive number that is evenly divisible by all of the
# numbers from 1 to 20?


#
from p3_largest_prime_factor import is_prime, is_factor

# extract 'element' which is an integer from an array of integers
# the array of elements is also an output
def extract_element_from( element, array_of_elements ) :
    output = []
    length = len( array_of_elements )
    end_of_list = ( length == 0 )
    found = False
    index = 0
    while ( not end_of_list ) and ( not found ) :
      if array_of_elements[ index ] == element :
        e = array_of_elements.pop( index )
        output.append( e )
        return output
        found = True
      else :
        index += 1
        if length == index :
          end_of_list = True
          return output

# to find the common elements between f1 and f2
# it returns the common elements,
#
# it shouldn't touch f1 or f2 although currently this is not done in a beautiful way
# the problem is that array.pop(n) when array was ana argument of the function is
# actually modified by pop.
def mcd( f1, f2 ) :
  common = []
  for index in xrange( 0, len( f1 ) ) :
    element = extract_element_from( f1[ index ], f2 )
    try :
      common = common + element
    except :
      common
      
  for i in xrange(0, len( common ) ) :
    f2.append( common[ i ] )

  return common

def not_mcd( factors_1, factors_2, common_divisors ) :
  for divisor in common_divisors :
    extract_element_from( divisor, factors_1 )
    extract_element_from( divisor, factors_2 )

  return factors_1 + factors_2

def prime_factors_of( multiple ) :
  factors = []
  maximum = multiple + 1
  while multiple <> 1 :
    for number in xrange( 2, maximum ) :
      if is_factor( number, multiple ) and is_prime( number ) :
        factors.append( number )
        multiple = multiple / number

  return factors

# minimum common multiple
# $first : integer
# $second : integer
def mcm( first, second ) :
  factors_1 = prime_factors_of( first )
  factors_2 = prime_factors_of( second )
  common_divisors = mcd( factors_1, factors_2 )
  not_common_divisors = not_mcd( factors_1, factors_2, common_divisors )
  all_divisors = common_divisors + not_common_divisors
  return reduce( lambda x,y: x * y, all_divisors )


if __name__ == "__main__" :
  n = 20  
  print "n: ", n
  multiple = 1 
  print "muliple: ", multiple
  for divisor in xrange( 2, n ) :
    print "divisor: ", divisor
    multiple = mcm( multiple, divisor )
    print "multiple: ", multiple

  print "The mcm is: ", multiple


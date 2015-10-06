#!/usr/bin/python
# Project Euler (projecteuler.net)
#
# Problem 8: Largest product in a series
#
# The four adjacent disgits in the 1000-digit number that have the greatest
# product are 9 x 9 x 8 x 9 = 5832.
# 73167176531330624919225119674426574742355349194934
# 96983520312774506326239578318016984801869478851843
# 85861560789112949495459501737958331952853208805511
# 12540698747158523863050715693290963295227443043557
# 66896648950445244523161731856403098711121722383113
# 62229893423380308135336276614282806444486645238749
# 30358907296290491560440772390713810515859307960866
# 70172427121883998797908792274921901699720888093776
# 65727333001053367881220235421809751254540594752243
# 52584907711670556013604839586446706324415722155397
# 53697817977846174064955149290862569321978468622482
# 83972241375657056057490261407972968652414535100474
# 82166370484403199890008895243450658541227588666881
# 16427171479924442928230863465674813919123162824586
# 17866458359124566529476545682848912883142607690042
# 24219022671055626321111109370544217506941658960408
# 07198403850962455444362981230987879927244284909188
# 84580156166097919133875499200524063689912560717606
# 05886116467109405077541002256983155200055935729725
# 71636269561882670428252483600823257530420752963450
#
# Find the thirteen adjacent digits in the 1000-digit number that have the
# greatest product. What is the value of this product?

import re

# The number to read is expected to be in a file and can be split into multiple lines.
def read_number( filepath ) :
  numbers_file = open( filepath, 'r')
  long_number = ''
  for line in numbers_file :
    long_number = long_number + line.rstrip( '\n' )

  return list( long_number )


def partition( array, window_size ) :
  partitioned = []
  for window_number in xrange( 0, len( array ) - window_size + 1 ) :
    windowed_element = array[ window_number:window_number + window_size ]
    partitioned.append( windowed_element )

  return partitioned 


def partition_13( array ) :
  return partition( array, 13 )


if __name__ == "__main__" :
  array = read_number( "/home/iwi/projectes/project_euler/p8_numbers")
  partitioned = partition_13( array )
  products = map( lambda element: reduce( lambda x,y: int( x ) * int( y ), element ), partitioned )
  maximum = reduce( lambda x,y: max( x, y ), products )
  print "The maximum product is", maximum


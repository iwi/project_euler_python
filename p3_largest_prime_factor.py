#!/usr/bin/python                                                                     
# Project Euler (projecteuler.net)
#
# Problem 3: Largest prime factor
#
# The prime factors of 13195 are 5, 7, 13 and 29.
#
# What is the largest prime factor of the number 600851475143 ?


# algorithm to check if a number is prime that only needs to check one every
# six integers
def is_prime(n) :
  if n == 2 or n == 3 or n == 5 :
    return True
  elif n < 2 :
    return False
  elif n % 2 == 0 :
    return False
  elif n % 3 == 0 :
    return False
  elif n % 5 == 0 :
    return False
  else :
    f = 5
    while f < int( n ** 0.5 ) :
      if n % f == 0 :
        return False
      elif n % ( f + 2 ) == 0 :
        return False
      f += 6
    return True

def is_factor(n, m) :
  integer_division = m / n
  float_division = float( m ) / n
  return integer_division == float_division

def largest_prime_factor( m ) :
  f = int( m ** 0.5 )
  while f > 1 :
    print f, ' ', is_factor(f, m), ' ', is_prime(f)
    if is_factor( f, m ) & is_prime( f ) :
      return f
      break
    else :
      if f % 2 == 0 :
        f -= 1
      else :
        f -= 2
  return m

if __name__ == "__main__" :
  m = 600851475143 
  f = largest_prime_factor( m ) 
  print 'the largest prime factor of ', m, ' is ', f

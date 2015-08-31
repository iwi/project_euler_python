#!/usr/bin/python 
# Project Euler (projecteuler.net)
#
# Problem 2: Even Fibonacci numbers 
#
#
# Each new term in the Fibonacci sequence is generated by adding the previous
# two terms. By starting with 1 and 2, the first 10 terms will be:
# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
#
# By considering the terms in the Fibonacci sequence whose values do not exceed
# four million, find the sum of the even-valued terms.

def fib(minus_one, minus_two):
  return minus_one + minus_two

minus_two = 0 
minus_one = 1
current = 2
big_sum = 0
maxim = 4000000

while current < maxim :
  if current % 2 == 0 : big_sum += current
  minus_two = minus_one
  minus_one = current
  current = minus_one + minus_two

if __name__ == "__main__":
  print big_sum
    

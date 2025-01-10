#!/usr/bin/env python3

# HackerRank: 30 Days of Code: Day 9: Recursion 3
# Problem: https://www.hackerrank.com/challenges/30-recursion/problem



import math
import os
import random
import re
import sys

#
# Complete the 'factorial' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

############################################################
def factorial(n):
    # Write your code here
    if 1 == n:
        result = 1
    else:
        result = n * factorial(n-1)

    return result
############################################################

############################################################
if __name__ == '__main__':
    n = int(input().strip())
    result = factorial(n)
    print(result)
############################################################
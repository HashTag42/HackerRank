# HackerRank: 30 Days of Code: Day 29 Bitwise AND
# Problem: https://www.hackerrank.com/challenges/30-bitwise-and/problem?isFullScreen=true

#!/bin/python3

import os

#
# Complete the 'bitwiseAnd' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER N
#  2. INTEGER K
#

FILE = "test.txt"

def bitwiseAnd(N, K):
    # Write your code here
    max = 0
    for i in range (1, N+1):
        for j in range (i+1, N+1):
            result = i & j
            if result > max and result < K:
                max = result
    return max

if __name__ == '__main__':

    fptr = open(FILE, 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        count = int(first_multiple_input[0])

        lim = int(first_multiple_input[1])

        res = bitwiseAnd(count, lim)

        fptr.write(str(res) + '\n')

    fptr.close()




# HackerRank challenge: https://www.hackerrank.com/challenges/array-left-rotation/problem?isFullScreen=true

#!/bin/python3

import os

#
# Complete the 'rotateLeft' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER d
#  2. INTEGER_ARRAY arr
#

def rotateLeft(d, arr):
    # Write your code here
    n = len(arr)
    for i in range(d):
        temp = arr[0]
        for j in range(n-1):
            arr[j] = arr[j+1]
        arr[n-1] = temp
    return arr
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    d = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    result = rotateLeft(d, arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

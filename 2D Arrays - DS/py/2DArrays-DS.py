# HackerRank challenge: https://www.hackerrank.com/challenges/2d-array/problem?isFullScreen=true=true

#!/bin/python3

import os

#
# Complete the 'hourglassSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#
def hourglassSum(arr):
    # Write your code here
    max = float('-inf')
    for x in range (len(arr) - 2):
        for y in range (len(arr[x]) - 2):
            single = singleHourglassSum(arr, x, y)
            if single > max:
                max = single
    return max

def singleHourglassSum(arr, x, y):
    total = 0
    for col in range(y, y+3):
        total += arr[x][col]
        total += arr[x+2][col]
    total += arr[x+1][y+1]
    return total

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()



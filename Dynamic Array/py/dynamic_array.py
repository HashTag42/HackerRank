# HackerRank challenge: https://www.hackerrank.com/challenges/dynamic-array/problem?isFullScreen=true
# !!! Note: The challenge instructions fail to mention that idx needs to be modulo the size of the array

#!/bin/python3

import os


#
# Complete the 'dynamicArray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#

def dynamicArray(n, queries):
    # Write your code here
    answers = list()
    lastAnswer = 0

    arr = [0] * n
    for i in range(n):
        arr[i] = []

    for q in queries:
        query_type, x, y = q[0], q[1], q[2]
        idx = (x ^ lastAnswer) % n  # See note at the top of this file
        if   query_type == 1:
            arr[idx].append(y)
        elif query_type == 2:
            lastAnswer = arr[idx][y % len(arr[idx])]
            answers.append(lastAnswer)
    return answers


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    q = int(first_multiple_input[1])

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    result = dynamicArray(n, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

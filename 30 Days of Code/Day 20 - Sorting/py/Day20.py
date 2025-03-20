# HackerRank: 30 Days of Code: Day 20: Sorting
# Problem: https://www.hackerrank.com/challenges/30-sorting/problem?isFullScreen=true

#!/bin/python3

import math
import os
import random
import re
import sys


if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    # Write your code here
    totalSwaps = 0
    for i in range(n):
        # Track number of elements swapped during a single array traversal
        numberOfSwaps = 0
        for j in range(n-1):
            # Swap adjacent elements if they are in decreasing order
            if (a[j] > a[j+1]):
                temp   = a[j]
                a[j]   = a[j+1]
                a[j+1] = temp
                numberOfSwaps += 1
                totalSwaps += 1

        if (numberOfSwaps == 0):
            break

print(f"Array is sorted in {totalSwaps} swaps.")
print(f"First Element: {a[0]}")
print(f"Last Element: {a[n-1]}")
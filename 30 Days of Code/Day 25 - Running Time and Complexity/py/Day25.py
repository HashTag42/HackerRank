# HackerRank: 30 Days of Code: Day 25: Running Time and Complexity
# Problem: https://www.hackerrank.com/challenges/30-running-time-and-complexity/problem?isFullScreen=true

# Enter your code here. Read input from STDIN. Print output to STDOUT

import math

def isPrime(number):
    if number < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if number % i == 0:
            return False
    return True

T = int(input().strip())
for i in range(T):
    n = int(input().strip())
    if isPrime(n):
        print("Prime")
    else:
        print("Not prime")
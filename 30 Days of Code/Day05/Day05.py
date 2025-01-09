# HackerRank: 30 Days of Code - Day 5: Loops
# Problem: https://www.hackerrank.com/challenges/30-loops/problem?isFullScreen=true

#!/bin/python3

def printMultiples(n):
    for i in range(1,11):
        print(f"{n} x {i} = {n * i}")


if __name__ == '__main__':
    n = int(input().strip())
    printMultiples(n)
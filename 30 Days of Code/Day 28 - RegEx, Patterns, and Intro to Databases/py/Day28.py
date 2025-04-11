# HackerRank: 30 Days of Code: Day 28: RegEx, Patterns, and Intro to Databases
# Problem: https://www.hackerrank.com/challenges/30-regex-patterns/problem?isFullScreen=true

#!/bin/python3

import re

if __name__ == '__main__':
    N = int(input().strip())

    name = []

    for N_itr in range(N):
        first_multiple_input = input().rstrip().split()

        firstName = first_multiple_input[0]

        emailID = first_multiple_input[1]

        if re.search(r"@gmail\.com", emailID):
            name.append(firstName)

    name.sort()
    for i in name:
        print(i)

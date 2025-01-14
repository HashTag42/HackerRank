# HackerRank: 30 Days of Code: Day 11: 2D Arrays
# Problem: https://www.hackerrank.com/challenges/30-2d-arrays/problem

#!/bin/python3

def AddupHourglass(x,y):
    return (arr[x  ][y  ] + arr[x  ][y+1] + arr[x  ][y+2] +
                            arr[x+1][y+1] +
            arr[x+2][y  ] + arr[x+2][y+1] + arr[x+2][y+2])

if __name__ == '__main__':

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    maximum = -100   # We need a number lower than the minimum Hourglass sum of 9 x -9 =-81.

    for x in range(4):
        for y in range(4):
            maximum = max(maximum, AddupHourglass(x,y))

    print(maximum)
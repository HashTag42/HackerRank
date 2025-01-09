# HackerRank 30 days of code Day 7: Arrays
# Problem: https://www.hackerrank.com/challenges/30-arrays/problem

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    for i in range (n, 0, -1):
        print(arr[i-1], end=" ")

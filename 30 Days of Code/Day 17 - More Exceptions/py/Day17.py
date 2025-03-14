# HackerRank: 30 Days of Code: Day 17: More Exceptions
# Problem: https://www.hackerrank.com/challenges/30-more-exceptions/problem?isFullScreen=true

#Write your code here
class Calculator():
    # def __init__(self):
    def power(self, n, p):
        if n < 0 or p < 0:
            raise ValueError("n and p should be non-negative")
        result = 1
        for x in range(p):
            result *= n
        return result

myCalculator=Calculator()
T=int(input())
for i in range(T):
    n,p = map(int, input().split())
    try:
        ans=myCalculator.power(n,p)
        print(ans)
    except Exception as e:
        print(e)
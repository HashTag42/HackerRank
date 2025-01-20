# HackerRank: 30 Days of Code: Day 14: Scope
# Problem: https://www.hackerrank.com/challenges/30-scope/problem

class Difference:
    def __init__(self, a):
        self.__elements = a
        self.maximumDifference = 0

	# Add your code here
    def computeDifference(self):
        for i in range(len(a)-1):
            for j in range(i,len(a)):
                dif = abs(a[i] - a[j])
                if(dif > self.maximumDifference):
                    self.maximumDifference = dif
# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)
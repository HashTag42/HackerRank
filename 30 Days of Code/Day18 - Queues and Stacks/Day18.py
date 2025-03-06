# HackerRank: 30 Days of Code: Day 18: Queues and Stacks
# Problem: https://www.hackerrank.com/challenges/30-queues-stacks/problem?isFullScreen=true

import sys
from queue import Queue

class Solution:
    # Write your code here
    def __init__(self):
        self.queue = Queue()
        self.stack = []
    def pushCharacter(self, c):
        return self.stack.append(c)
    def popCharacter(self):
        return self.stack.pop()
    def enqueueCharacter(self, c):
        return self.queue.put(c)
    def dequeueCharacter(self):
        return self.queue.get()

# read the string s
s=input()
#Create the Solution class object
obj=Solution()

l=len(s)
# push/enqueue all the characters of string s to stack
for i in range(l):
    obj.pushCharacter(s[i])
    obj.enqueueCharacter(s[i])

isPalindrome=True
'''
pop the top character from stack
dequeue the first character from queue
compare both the characters
'''
for i in range(l // 2):
    if obj.popCharacter()!=obj.dequeueCharacter():
        isPalindrome=False
        break
#finally print whether string s is palindrome or not.
if isPalindrome:
    print("The word, "+s+", is a palindrome.")
else:
    print("The word, "+s+", is not a palindrome.")
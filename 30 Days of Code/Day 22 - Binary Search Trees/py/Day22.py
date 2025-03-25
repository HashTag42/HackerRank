# HackerRank: 30 Days of Code: Day 21: Binary Search Trees
# Problem: https://www.hackerrank.com/challenges/30-sorting/problem?isFullScreen=true

class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data
class Solution:
    def insert(self,root,data):
        if root==None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root

    def getHeight(self,root):
        #Write your code here
        height = 0
        if root == None:
            return -1
        else:
            lHeight = self.getHeight(root.left)
            rHeight = self.getHeight(root.right)
            height  = 1 + max(lHeight, rHeight)
        return height

T=int(input())
myTree=Solution()
root=None
for i in range(T):
    data=int(input())
    root=myTree.insert(root,data)
height=myTree.getHeight(root)
print(height)  
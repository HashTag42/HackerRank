# HackerRank: 30 Days of Code: Day 24 More Linked Lists
# Problem: https://www.hackerrank.com/challenges/30-linked-list-deletion/problem?isFullScreen=true

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None 
class Solution: 
    def insert(self,head,data):
            p = Node(data)           
            if head==None:
                head=p
            elif head.next==None:
                head.next=p
            else:
                start=head
                while(start.next!=None):
                    start=start.next
                start.next=p
            return head  
    def display(self,head):
        current = head
        while current:
            print(current.data,end=' ')
            current = current.next

    def removeDuplicates(self,head):
        #Write your code here
        source = head
        while source:
            current = source
            while current and current.next:
                if current.data == current.next.data:
                    current.next = current.next.next
                else:
                    current = current.next
            source = source.next
        return head

mylist= Solution()
T=int(input())
head=None
for i in range(T):
    data=int(input())
    head=mylist.insert(head,data)    
head=mylist.removeDuplicates(head)
mylist.display(head); 

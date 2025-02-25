# HackerRank: 30 Days of Code: Day 15: Linked List
# Problem: https://www.hackerrank.com/challenges/30-linked-list/problem

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class Solution:
    def display(self,head):
        current = head
        while current:
            print(current.data,end=' ')
            current = current.next

    def insert(self,head,data):
        if head is None:
            head = Node(data)
            head.next = None
        else:
            # Find the last node
            last = None
            current = head
            while current:
                last = current
                current = current.next
            # Link last node to the new one
            last.next = Node(data)
        return head

if __name__ == "__main__":
    mylist= Solution()
    T=int(input())
    head=None
    for i in range(T):
        data=int(input())
        head=mylist.insert(head,data)
    mylist.display(head);
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
    def insert(self, head, data):
        # Complete this method
        current = head
        n = Node(data)
        if head == None:
            head = n
            return(head)
        else:
            while current:
                if current.next is None:
                    current.next = n
                    return(head)
                else:
                    current = current.next
mylist= Solution()
T=int(input())
head=None
for i in range(T):
    data=int(input())
    head=mylist.insert(head,data)
mylist.display(head)
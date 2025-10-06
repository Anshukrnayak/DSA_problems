
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None
        self.count=0

    def push(self,data):
        new_node=Node(data)
        new_node.next=self.head
        self.head=new_node

    def middle_node(self):
        if self.head is None:
            raise ValueError('No list')
        fast_node = self.head
        slow_node = self.head

        while fast_node is not None and fast_node.next is not None:
            slow_node = slow_node.next
            fast_node = fast_node.next.next
        return slow_node

    def reverse_list(self):
        if self.head is None:
            raise ValueError('No list : ')
        previous=None
        start=self.middle_node()
        while start is not None:
            next_node=start.next
            start.next=previous
            previous=start
            start=next_node
        return previous

    def is_palindrome(self):
        if self.head is None:
            raise ValueError('No list')
        first_node=self.head
        second_node=self.reverse_list()

        while first_node is not None and second_node is not None:
            if first_node.data!=second_node.data:
                 return False
            first_node=first_node.next
            second_node=second_node.next
        return True

arr=[1,2,3,3,2,1]
l=LinkedList()

for data in arr: l.push(data)
print(l.is_palindrome())
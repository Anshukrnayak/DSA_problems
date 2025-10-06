import numpy as np
class Node:
    def __init__(self,data):
        self.data=data 
        self.next=None

# creating linked list 

class LinkedList:
    def __init__(self): self.head=None # constructor function 

    def inseartion(self,data):
        new_node=Node(data)
        new_node.next=self.head
        self.head=new_node

    
    def create_circular_list(self,pos):
        temp=self.head
        for i in range(0,pos-1):
            temp=temp.next

        index=self.head
        while index.next is not None: index=index.next
        index.next=temp

    def check_circular_list(self):
        first=self.head
        slow=self.head

        while first.next is not None and slow.next is not None:
            if slow==first: return True
            slow=slow.next
            fast=fast.next.next
        return False

    def dislay_list(self):
        temp=self.head
        while temp is not None:
            print(temp.data)
            temp=temp.next

def main():
    arr=np.arange(15)
    l=LinkedList()
    for i in arr: l.inseartion(i)

    l.create_circular_list(7)
    ans=l.check_circular_list()

    print(f'Is circular list : {ans}')

if __name__=='__main__': main()



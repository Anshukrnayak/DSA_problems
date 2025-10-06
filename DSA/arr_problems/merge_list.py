import numpy as np

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None


class LinkedList:
    def __init__(self): self.head=None

    def insertion_head(self,data):
        
        new_node=Node(data)
        new_node.next=self.head
        self.head=new_node


    def mid_node(self):

        if self.head is None: return self.head

        slow=self.head 
        fast=self.head

        while fast is not None and fast.next is not None:
            slow=slow.next 
            fast=fast.next.next 
        
        return slow

    def merge_two_list(left,right):
        
        new_list=LinkedList()

        while left is not None and right is not None:
            if left.data<right.dat:
               new_list.insertion_head(left.data)
               left=left.next
            else:
                new_list.insertion_head(left.head)
                righ=right.next 
        

        return new_list


    def merger_sort(self,node):
        
        if node.next is None: return node

        first_list=self.head
        second_list=self.mid_node()

        left_list=self.merger_sort(first_list)
        right_list=self.merger_sort(second_list)

        self.merge_two_list(left_list,righ_list)


    def display_list(self):

        temp=self.head
        while temp is not None: 
            print(temp.data)
            temp=temp.next


def main():
    arr=[2,4,1,3,5,0]
    l=LinkedList()

    for i in arr: l.insertion_head(i)

    l.display_list()
    new_list=l.merger_sort(l.head)

    l.display_list()


if __name__=='__main__': main()
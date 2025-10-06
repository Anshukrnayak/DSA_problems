
import numpy as np

class node:
    def __init__(self,data):
        self.data=data 
        self.next=None
    


class linked_list:
    def __init__(self):
        self.head=None
        self.size=0

    def insertion_head(self,data):
        
        temp=node(data)
        temp.next=self.head
        self.head=temp
    
    def insertion_tail(self,data):

        new_node = node(data) 
        if self.head is None:  
            self.head = new_node  
            return


        last_node = self.head
        
        while last_node.next:  
            last_node = last_node.next
        last_node.next = new_node

    def insertion_at_middle(self,data,count):

        if self.head is None: return self.insertion_head(data)

        if self.head.next is None: return self.insertion_tail(data)

        new_node=node(data)
        
        temp=self.head 
        for i in range(0,count-1):
            temp=temp.next
        
        next_next=temp.next 
        temp.next=new_node
        new_node.next=next_next


    def display_list(self):
        temp=self.head
        while temp is not None:
            print(temp.data)
            temp=temp.next



def main():
    arr=np.arange(5)
   
    l=linked_list()

    
    for i in arr: l.insertion_tail(i)

    l.insertion_at_middle(5,5)



    l.display_list()


if __name__=='__main__': main()


        


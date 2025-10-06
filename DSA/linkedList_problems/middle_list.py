import numpy as np

class node:
    def __init__(self,data):
        self.data=data
        self.next=None

class linked_list:
    def __init__(self):
        self.head=None
        self.next=0
    
    def insert_head(self,data):
        if self.head is not None:
            
            newnode=node(data)
            newnode.next=self.head
            self.head=newnode
            
    def display(self):
        temp=self.head
        
        while temp is not None:
            print(temp.data )
            temp=temp.next
    
    def middle_list(self):
    
        slow=self.head
        fast=self.head
        
        while fast is not None:
            fast=fast.next
            slow=slow.next
            
            if fast is not None:
                fast=fast.next
        
        return slow
        
        


def main():
    arr=np.arange(10)
  
    l=linked_list
    
    for i in arr:
        l.insert_head(i)
        
    l.display()

if __name__=='__main__': main()
    

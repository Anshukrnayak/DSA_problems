
import numpy as np

class node:
    def __init__(self,data):
        self.data=data
        self.next=None
        

class linked_list:
    def __init__(self):
        self.head=None
        self.next=None
        
    def insert(self,data):
        newNode=node(data)
        newNode.next=self.head
        self.head=newNode
    
    def display(self):
        temp=self.head
        
        while temp is not None:
            print(temp.data)
            temp=temp.next
    
def main():
    arr=np.arange(10)
    
    l=linked_list()
    for i in arr:
        l.insert(i)
        
    l.display()

if __name__=='__main__': main()


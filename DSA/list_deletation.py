
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
    
    def delete_node(self,pos):

        temp=self.head
        for i in range(0,pos-1):
            temp=temp.next 
        
        del_node=temp.next
        temp.next=del_node.next 
        del del_node


    def relplace_data(self,data,pos):

        temp=self.head 
        for i in range(0,pos-1):
            temp=temp.next 
        
        replace_index=temp.next 
        replace_index.data=data 

        return 

    def display(self):
        temp=self.head 
        while temp is not None:
            print(temp.data)
            temp=temp.next 



def main():
    arr=[3,1,2,3,4,5]
    l=linked_list()
    for i in arr: l.insertion_head(i)

    l.delete_node(2)
    l.relplace_data(2,2)
    l.display()


if __name__=='__main__': main()
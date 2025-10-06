
class node:
    def __init__(self,data):
        self.data=data 
        self.next=None


class linked_list:

    def __init__(self): self.head=None

    def insertion(self,data):

        new_node=node(data)
        new_node.next=self.head
        self.head=new_node
    

    def bubble_sort(self):

        i=self.head 

        while i is not None:
            j=i 
            while j.next is not None:
                if j.data>j.next.data:
                    j.data,j.next.data=j.next.data,j.data
                j=j.next 
            i=i.next


    def display_list(self):
        temp=self.head 

        while temp is not None:
            print(temp.data)
            temp=temp.next 
            

def main():
    arr=[4,3,2,1,5]
    l=linked_list()

    for i in arr: l.insertion(i)

    l.bubble_sort()
    l.display_list()
        

if __name__=='__main__': main()

class node:
    def __init__(self,data):
         self.data=data 
         self.next=None


class linked_list:
    def __init__(self): self.head=None


    def insertion_head(self,data):
        new_node=node(data)
        new_node.next=self.head 
        self.head=new_node
    

    def reverse_list(self):
        prev=None
        start=self.head 

        while start is not None:
            next_node=start.next
            start.next=prev
            prev=start
            start=next_node

        return prev



    def display_list(self):
        temp=self.reverse_list()
        while temp is not None:
            print(temp.data)
            temp=temp.next


def main():
    arr=[1,2,3,4,5]
    l=linked_list()

    for i in arr: l.insertion_head(i)

    l.display_list()

if __name__=='__main__': main()



class node:
    def __init__(self,data):
        self.data=data 
        self.next=None


class linked_list:
    def __init__(self):
        self.head=None
        self.size=0
    

    def insertion_head(self,data):

        new_node=node(data)
        new_node.next=self.head
        self.head=new_node

    def display_list(self):
        temp=self.head

        while temp is not None:
            print(temp.data)
            temp=temp.next
    

    def list_sum(self):
        temp=self.head 
        sum=0

        while temp is not None:
            sum+=temp.data
            temp=temp.next
        
        return sum
    

    # first approach : 
    def odd_sum(self):
        fast=self.head 
        sum=0


        while fast.next is not None:
            print(fast.data)
            sum+=fast.data
            fast=fast.next.next 

        return sum

    # second approach 

    def odd_sum(self):
        current=self.head 
        index=0
        sum=0

        while current is not None:
         
            if index%2==0: sum+=current.data
            
            index+=1
            current=current.next
        
        return sum


    def even_sum(self):
        current=self.head
        index=0
        sum=0 

        while current is not None:
            if index%2!=0: sum+=current.data

            current=current.next
            index+=1
            
        return sum



def main():
    arr=[1,2,3,4,5,6,7]
    l=linked_list()

    for i in arr: l.insertion_head(i)

    ans=l.even_sum()
    print(len(l))
    
    print(f'sum of the list : {ans}')


if __name__=='__main__': main()
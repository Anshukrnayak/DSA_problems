
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

    def display(self):
        temp=self.head
    
        while temp is not None:
            print(temp.data)
            temp=temp.next

    # first  approach  : 

    def convert_linked_list_to_arr(self):
        temp=self.head
        arr=[]

        while temp is not None:
            arr.append(temp.data)
            temp=temp.next

        return arr

    def palindrome_list(self):
        arr=self.convert_linked_list_to_arr()

        s=0
        e=len(arr)-1

        while s<=e:
            if arr[s]!=arr[e]: return False 
            s+=1
            e-=1
        
        return True

    # second approach 

    
    def mid_node(self):
        fast=self.head
        slow=self.head 

        while fast is not None:
            slow=slow.next 
            fast=fast.next.next 
        
        return slow

    def reverse_list(self):
        prev=None
        start=self.mid_node()

        while start is not None:
            next_next=start.next
            start.next=prev
            prev=start
            start=next_next
        
        return prev


    def palindrome_list(self):
        first_list=self.head
        second_list=self.reverse_list()

        while first_list is not None and second_list is not None: 
            if first_list.data!=second_list.data: return False 
                    
            first_list=first_list.next
            second_list=second_list.next
        
        return True


def main():
    arr=[1,2,3,3,2,1]
    l=linked_list()
    for i in arr: l.insertion(i)

    ans=l.palindrome_list()
    print(f'is palindrome : {ans} ')
    

if __name__=='__main__': main()
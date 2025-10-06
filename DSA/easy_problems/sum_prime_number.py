
# sum of prime using linked list : 




class node:

    def __init__(self,data):
        self.data=data
        self.next=None
    


class linked_list:

    def __init__(self):
        self.head=None
        self.size=0
    


    def insertion(self,data):

        temp=node(data)
        temp.next=self.head
        self.head=temp
    

    def display(self):

        temp=self.head

        while temp is not None:
            print(temp.data)
            temp=temp.next
    

    def sum_prime(self):
        sum=0
        i=2
        temp=self.head

        while temp is not None:
            
            if temp.data%i==0:
                 sum+=temp.data

            temp=temp.next
            i+=1
        
        return sum;

    

def main():

    import numpy as np

    arr=np.array([1,2,3,4,5,6])
  
    l=linked_list()

    for i in arr:
        l.insertion(i)
    
    sum=l.sum_prime()

    print(f'The sum of prime numbers : {sum} ')



if __name__=='__main__': main()





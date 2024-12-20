

class node:
    def __init__(self,data):
        self.data=data
        self.next=None


class linked_list:

    def __init__(self):
        self.head=None

    def insertion_head(self,data):
        temp=node(data)
        temp.next=self.head
        self.head=temp

    def selection_sort(self):
        i=self.head
        while i is not None:
            j=i.next 

            while j is not None:
                if i.data<j.data:
                    i.data,j.data=j.data,i.data 
                
                j=j.next 

            i=i.next 

    def display_list(self):
        temp=self.head 

        while temp is not None:
            print(temp.data)
            temp=temp.next


def main():
    arr=[3,2,1,4,5]
    l=linked_list()

    for i in arr: l.insertion_head(i)

    l.selection_sort()
    l.display_list()



if __name__=='__main__': main()

class Node:
   def __init__(self,data):
      self.data=data
      self.next=None

class Stack:
   def __init__(self):
      self.head=None

   def push(self,data):
      new_node=Node(data)
      new_node.next=self.head
      self.head=new_node

   def pop(self):
      if self.head is None:
         raise IndexError('Stack is empty')
      data=self.head.data
      self.head=self.head.next
      return data

   def peek(self):
      if self.head is None:
         raise IndexError('Stack is Empty ')
      return self.head.data

   def length_list(self):

      if self.head is None:
         raise IndexError('Stack is empty')
      temp=self.head
      count=0
      while temp is not None:
         temp=temp.next
         count+=1
      return count

   def get_list_data(self):
      if self.head is None:
         raise IndexError('Stack is empty')

      temp=self.head
      while temp is not None:
         print(temp.data)
         temp=temp.next


def main():
   arr=[data for data in range(0,10) if data%2==0]
   s=Stack()
   for data in arr: s.push(data)

   for _ in range(0,s.length_list()): print(s.pop())

if __name__=='__main__': main()

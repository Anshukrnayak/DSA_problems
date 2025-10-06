class Node:
   def __init__(self, data):
      self.data = data
      self.next = None


class QueueList:
   def __init__(self):
      self.front = None
      self.rear = None

   def push(self, data):
      new_node = Node(data)
      if self.rear is None:
         self.front = self.rear = new_node
         return
      self.rear.next = new_node
      self.rear = new_node

   def pop(self):
      if self.front is not None:
         temp = self.front
         self.front = self.front.next
         if self.front is None:  # If the queue is now empty
            self.rear = None
         return temp.data

      raise IndexError('Queue is empty')

   def peek(self):
      if self.front is None:
         raise IndexError('Queue is empty')

      return self.front.data

   def is_empty(self):
      return self.front is None


def main():
   q = QueueList()
   for data in range(10):  # Adding elements 0 to 9
      q.push(data)

   print(q.pop())  # Outputs: 0
   print(q.pop())  # Outputs: 1
   print(q.pop())  # Outputs: 2


if __name__ == '__main__':
   main()


class Node:
   def __init__(self,data):
      self.data=data
      self.left=None
      self.right=None



def main():
   a=Node(1)
   b=Node(2)
   c=Node(3)
   d=Node(4)
   e=Node(5)
   f=Node(6)

   a.left=b
   a.right=c
   b.left=d
   b.right=e
   c.right=f



if __name__=='__main__': main()
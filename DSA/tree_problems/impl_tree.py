from collections import deque
import queue

class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

# DFS

def in_order_traversal(root):
    if root is None:
        return

    in_order_traversal(root.left)
    print(root.data)
    in_order_traversal(root.right)


def height(root):
    if root is None:
        return 0

    left=height(root.left)
    right=height(root.right)

    return max(left,right)+1

# level order traversal :

def level_order_traversal(root):
    q=deque([])
    level=[]
    q.append(root)

    while q:
        q_length=len(q)
        for _ in range(q_length):
            node=q.popleft()
            if node:
                level.append(node.data)
                q.append(node.left)
                q.append(node.right)

    return level

def main():
    a=Node(1)
    b=Node(2)
    c=Node(3)
    d=Node(4)
    e=Node(5)
    f=Node(6)
    g=Node(7)

    a.left=b
    a.right=c
    b.left=d
    b.right=e
    d.left=f
    d.right=g

    print(level_order_traversal(a))

if __name__=='__main__': main()
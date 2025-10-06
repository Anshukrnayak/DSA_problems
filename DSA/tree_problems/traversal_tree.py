from collections import deque

class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None


# DFS # depth first search
def in_order_traversal(root):
    if root is None:
        return

    in_order_traversal(root.left)
    print(root.data)
    in_order_traversal(root.right)

# BFS level order traversal
def level_order_traversal(root):
    q=deque([])
    level=[]
    q.append(root)

    while q:
        size_length=len(q)
        for _ in range(size_length):
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
    h=Node(8)

    a.left=b
    a.right=c
    b.left=d
    b.right=e
    d.left=f
    d.right=g
    e.left=h

    print(level_order_traversal(a))

if __name__=='__main__': main()
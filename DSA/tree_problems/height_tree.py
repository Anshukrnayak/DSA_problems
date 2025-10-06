from collections import deque

class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def height_recursive(root):
    if root is None: return 0
    return max(height_recursive(root.left),height_recursive(root.right))+1

class Solution:

    def max_diameter(self, root):
        diameter = 0  # Outer variable to track max diameter

        def height(root):
            nonlocal diameter  # Tell Python to use the outer `diameter`
            if root is None:
                return 0
            left_height = height(root.left)
            right_height = height(root.right)
            diameter = max(diameter, left_height + right_height)  # Now this updates the outer `diameter`

            return max(left_height, right_height) + 1  # Return height of current node

        height(root)  # Call the helper function to compute diameter
        return diameter

    def balance_binary_tree(self,root):
        result=True
        def height(root):
            nonlocal result  # Tell Python to use the outer `diameter`
            if root is None:
                return 0
            left=height(root.left)
            right=height(root.right)
            if abs(left-right)>1:
                result=False

            return max(left,right)+1

        height(root)
        return result


def height_iteration(root):
    if root is None:
        return 0

    q=deque([])
    q.append(root)
    height=0

    while q:
        size=len(q)
        height+=1
        for _ in range(size):
            node=q.popleft()
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
    return height





def main():
    a = Node(1)
    b = Node(2)
    c = Node(3)
    d = Node(4)
    e = Node(5)
    f = Node(6)
    g = Node(7)

    a.left=b
    a.right=c
    b.left=d
    b.right=e
    c.left=f
    c.right=g



if __name__=='__main__': main()

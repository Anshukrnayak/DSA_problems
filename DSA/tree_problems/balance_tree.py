
class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def Is_balance_tree(root):
    def dsf(root):
        if root is None:
            return [True,0]
        left,right=dsf(root.left),dsf(root.right)
        balanced=left[0] and right[0] and abs(left[1]-right[1])<=1
        return [balanced,max(left[1],right[1])+1]

    return dsf(root)[0]

def main():
    a = Node(1)
    b = Node(2)
    c = Node(3)
    d = Node(4)
    e = Node(5)
    f = Node(6)
    g = Node(7)

    a.left = b
    a.right = c
    b.left = d
    b.right = e
    d.left = f
    d.right = g

    print(Is_balance_tree(a))

if __name__=='__main__': main()

class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None


class Solution:

    def max_sum(self,root):
        mix=NegInf
        def height(root):
            nonlocal mix
            if root is None:
                return 0

            left = height(root.left)
            right = height(root.right)
            sum = left + right
            return max(mix, sum)
        return height(root)


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
    c.left = f
    c.right = g

    s=Solution
    print(s.max_sum(a))


if __name__=='__main__': main()

def diameter_tree(root):
    if not root:
        return
    def height(root):
        if not root:
            return [0,0]
        left=height(root.left)
        right=height(root.right)

        diameter=max(left[0],right[0],(left[1]+right[1]))
        return [diameter,max(left[1],right[1])+1]

    return height(root)[0]



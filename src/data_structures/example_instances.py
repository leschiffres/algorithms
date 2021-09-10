class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

bt1 = TreeNode(1)
bt2 = TreeNode(2)
bt3 = TreeNode(3)
bt4 = TreeNode(4)
bt5 = TreeNode(5)
bt6 = TreeNode(6)
bt7 = TreeNode(7)
bt8 = TreeNode(8)

bt1.left = bt2
bt1.right = bt3
bt2.left = bt4
bt2.right = bt5
bt3.right = bt6
bt5.left = bt7
bt5.right = bt8

binary_tree_1 = bt1
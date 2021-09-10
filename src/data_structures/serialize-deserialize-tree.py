# https://leetcode.com/problems/serialize-and-deserialize-bst/
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def serialize(root):
    
    return dfs(root)

def deserialize(data):
    data = data.split(',')
    if data[0] == '':
        return None

    root = TreeNode(int(data[0])) 
    
    for s in data[1:]:
        if s == '':
            continue
            
        val = int(s)
        
        node, parent = [root, root]

        while True:
            
            if val < parent.val:
                node = node.left
                if not node:
                    parent.left = TreeNode(val)
                    break
                else:
                    parent = node
            else:
                node = node.right
                if not node:
                    parent.right = TreeNode(val)
                    break
                else:
                    parent = node
        
    return root
            

def dfs(node):
    
    if not node:
        return ''
    
    s = str(node.val) + ','
    s += str(dfs(node.left)) + ','
    s += str(dfs(node.right)) + ','
    
    return s

root = TreeNode(2)

root.left = TreeNode(1)
root.right = TreeNode(5)

root.right.left = TreeNode(4)
root.right.right = TreeNode(6)

data = serialize(root)
print(data)
data.split(',')
new_root = deserialize(data)
new_data = serialize(new_root)
print(new_data)

from example_instances import binary_tree_1

def bfs(root):
	nodes = [root]
	while nodes:
		node = nodes.pop(0)
		print(node.val)

		if node.left:
			nodes.append(node.left)

		if node.right:
			nodes.append(node.right)

def dfs(node):

	if not node:
		return

	print(node.val)
	dfs(node.left)
	dfs(node.right)

print("Breadth First Search")
bfs(binary_tree_1)
print("Depth First Search")
dfs(binary_tree_1)
from example_instances import binary_tree_1

def bt_to_graph(root):
	graph = {}
	nodes = [(root, root.left),(root, root.right)]
	while nodes:
		parent, node = nodes.pop(0)
		if node:
			print(node.val)
			if parent.val not in graph.keys():
				graph[parent.val] = [node.val]
			else:
				graph[parent.val].append(node.val)

			if node.val not in graph.keys():
				graph[node.val] = [parent.val]
			else:
				graph[node.val].append(parent.val)

			nodes.append((node, node.left))
			nodes.append((node, node.right))
	return graph

graph = bt_to_graph(binary_tree_1)
print(graph)
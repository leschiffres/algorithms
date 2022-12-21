# https://leetcode.com/problems/house-robber-ii/
# Given a cycle graph where nodes have weights, the goal is to select
# a set of vertices that have no edge between them and their the total
# weight is maximized .
# The solution is based on the idea that for each node either we include
# it or exclude it. If we do not include it then the best weight until the current note
# is to consider the best possible weight until the previous node and if we include it,
# we consider the best possible weight until two nodes before + the weight of the current node.
# Also since it's a cycle we repeat the above procedure twice; once excluding the first node
# once excluding the last node.
# The reason for this is that we want to avoid including them both in the same solution 
# and that the best solution includes at most one of them.

def max_weight(weights):
    additive_weight = []
    additive_weight.append(weights[0])
    additive_weight.append(max(weights[1], weights[0]))

    for i in range(2, len(weights)):
        additive_weight.append(max(additive_weight[i-1], additive_weight[i-2] + weights[i]))

    print(additive_weight)
    return additive_weight[-1]

weights = [4,3,4,6,2,1,8]

print(max(max_weight(weights[:-1]), max_weight(weights[1:])))
# https://leetcode.com/problems/linked-list-cycle/

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# First idea to detect cycle in a list, is to use a hashset. Everytime we find a new node, we add it in the set.
# If we find a node that already is in the set then there is cycle. We have O(1) operations for checking and adding
# but we need additional memory
def hasCycle2(head):
    if not head:
        return False

    nodes = set()
    node = head

    while node:
        if node.val in nodes:
            print(f"Found cycle at node {node.val}")
            return True
        nodes.add(node.val)
        node = node.next

    return False


# Second idea is to use two pointers.
# The first pointer traverses the node list one by one starting from the first (walker)
# The second pointer traverses the node list two by two starting from the second (runner)
# If those two pointers meet at some point then there is a cycle.

# How can we prove that iff there is a cycle these two pointers will surely meet?
# let's see some examples
# 1. odd number of nodes 
#   e.g. 1-2-3-4-5-2
#       walker: 1-2-3-4
#       runner: 2-4-2-4
#   e.g 1-2-3-4-5-6-7-8-9-1
#       walker: 1-2-3-4-5-6-7-8-9
#       runner: 2-4-6-8-1-3-5-7-9
# 2. even number of nodes 
#   e.g. 1-2-3-4-5-6-2
#       walker: 1-2-3-4-5
#       runner: 2-4-6-3-5
#   e.g 1-2-3-4-5-6-7-8-9-10-1
#       walker: 1-2-3-4-5 -6-7-8-9-10
#       runner: 2-4-6-8-10-2-4-6-8-10
def hasCycle(head):
    if not head:
        return False
                
    walker = head
    runner = head.next
    while walker != runner:
        print(f'Walker: {walker.val}, Runner: {runner.val}')
        if not runner or not runner.next:
            return False
        walker = walker.next
        runner = runner.next.next
               
    print(f"Found cycle at node {walker.val}")
    return True

n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)
n4 = ListNode(4)
n5 = ListNode(5)
n6 = ListNode(6)

n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
n5.next = n6
n6.next = n2

print("Algorithm to detect cycle in list: 1-2-3-4-5-6-2")

hasCycle(n1)
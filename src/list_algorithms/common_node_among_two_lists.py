# https://leetcode.com/problems/intersection-of-two-linked-lists/

# given two lists (their respective head), find the one node that is common between them.

# we use two pointers, one pointing in the start of the first list, 
# one pointing in the start of the second list. Whenever the end is reached for any of the 
# pointers, we redirect this pointer to the start of the other list.
# it can be proven that at some point both pointers will converge to the same node at
# the intersection.

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def get_intersection(headA, headB):
	pa, pb = headA, headB
	while pa != pb:
		print('')
		if pa:
			print(f"Pointer 1: {pa.val}")
			pa = pa.next
		else:
			print("Redirecting Pointer 1 to the list B")
			pa = headB
				            
		if pb:
			print(f"Pointer 2: {pb.val}")
			pb = pb.next
		else:
			print("Redirecting Pointer 2 to the list A")
			pb = headA
	return pa

a1 = ListNode('a1')
a2 = ListNode('a2')
a1.next = a2

b1 = ListNode('b1')
b2 = ListNode('b2')
b1.next = b2
b3 = ListNode('b3')
b2.next = b3

c1 = ListNode('c1')
c2 = ListNode('c2')
c1.next = c2

a2.next = c1
b3.next = c1

node = get_intersection(a1, b1)
print('common node: ' + node.val)
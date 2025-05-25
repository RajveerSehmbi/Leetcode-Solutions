"""
class ListNode:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next
"""

# Recursion O(n)

def reverseList(head):

	if not head:
		return None

	new_head = head
	if head.next:
		new_head = reverseList(head.next)
		head.next.next = head
	head.next = None
	
	return new_head



# Iteration O(n)

cur_node = head
prev_node = None

while cur_node:

	next_node = cur_node.next
	cur.next = prev_node
	prev_node = cur_node
	cur_node = next_node

return prev_node

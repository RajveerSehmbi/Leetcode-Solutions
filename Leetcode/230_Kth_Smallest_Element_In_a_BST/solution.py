# InOrder DFSO(n)

def kthSmallest(root, k):
	
	values = []
	
	def in_order(node):
		if not node:
			return
		
		in_order(node.left)
		values.append(node.val)
		in_order(node.right)
	

	in_order(root)
	if k > len(values):
		return None
	return values[k - 1]

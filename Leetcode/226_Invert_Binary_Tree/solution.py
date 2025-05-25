# Recursion O(n)

def invertTree(root):
	
	if root is None:
		return None
	
	inverted_left = invertTree(root.left)
	inverted_right = invertTree(root.right)
	
	root.left = inverted_right
	root.right = inverted_left

	return root

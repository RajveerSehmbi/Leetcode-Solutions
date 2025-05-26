# Brute Force O(n^2)

def isValidBST(root):

	if not root:
		return True	

	return (find_largest(root.left) < root.val < find_smallest(root.right)) and isValidBST(root.left) and isValidBST(root.right)


def find_largest(node):
	
	if not node:
		return float("-inf")
	
	return max(node.val, find_largest(node.left), find_largest(node.right))

def find_smallest(node):
	
	if not node:
		return float("inf")

	return min(node.val, find_smallest(node.left), find_smallest(node.right))



# DFS O(n)

def isValidBST(root):
	
	def valid(node, left, right):
		if not node:
			return True
		if not (left < node.val < right):
			return False

		return valid(node.left, left, node.val) and valid(node.right, node.val, right)

	return valid(root, float("-inf"), float("inf")) 

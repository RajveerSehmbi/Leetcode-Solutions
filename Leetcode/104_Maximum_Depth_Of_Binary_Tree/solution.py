
def dfs(root, depth):

	if root is None:
		return depth
	
	return 1 +  max(dfs(root.left), dfs(root.right))



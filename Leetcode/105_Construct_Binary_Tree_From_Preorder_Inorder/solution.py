# Linear search for idx O(n^2)

def buildTree(preorder, inorder):

	if not preorder or not inorder:
		return None

	root = TreeNode(preorder[0])
	idx = 0
	for i, val in enumerate(inorder):
		if val == preorder[0]:
			idx = i
			break
	root.left = buildTree(preorder[1 : idx + 1], inorder[: idx])
	root.right = buildTree(preorder[idx + 1 :], inorder[idx + 1:])
	return root

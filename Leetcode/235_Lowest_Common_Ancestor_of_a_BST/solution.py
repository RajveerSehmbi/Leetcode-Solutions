# Recursion O(h)

def lca(root, p, q):
	if not root or not p or not q:
		return None
	elif max(p.val, q.val) < root.val:
		return lca(root.left, p, q)
	elif min(p.val, q.val) > root.val:
		return lca(root.right, p, q)
	return root

# BFS O(n)

def levelOrder(root):
	
	queue = deque()
	queue.append(root)
	res = []

	while queue:
		q_length = len(queue)
		level = []		

		for i in range(q_length):
			node = queue.popleft()
			if not node:
				continue
			level.append(node.val)
			queue.append(node.left)
			queue.append(node.right)
		if level:
			res.append(level)
	return res

1 -> 2 -> 3 -> 4
becomes 1 -> 4 -> 2 -> 3

1 -> 2 -> 3 -> 4 -> 5
becomes 1 -> 5 -> 2 -> 4 -> 3


# Brute Force O(n)
# O(n) space

order = []

cur = head

while cur:
	order.append(cur)
	cur = cur.next

l = 0
r = len(order) - 1

while r - l > 1:
	order[l].next = order[r]
	order[r].next = order[l+1]
	l += 1
	r -= 1
order[r].next = None

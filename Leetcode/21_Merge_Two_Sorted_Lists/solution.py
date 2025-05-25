# Iteration O(n+m)

1 -> 2 -> 4
1 -> 3 -> 4 -> 5


dummy = ListNode()
cur = dummy

while list1 and list2:
	
	if list1.val <= list2.val:
		cur.next = list1
		list1 = list1.next
		cur = cur.next
	else:
		cur.next = list2
		list2 = list2.next
		cur = cur.next

if list1:
	cur.next = list1
elif list2:
	cur.next = list2

return dummy.next

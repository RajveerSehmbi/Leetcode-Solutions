# Sort and Compare O(nlogn)

if len(s) != len(t):
	return False
s.sort()
t.sort()
for i in range(len(s)):
	if s[i] != t[i]:
		return False
return True






# Count characters O(n)

s_count = count(s)
t_count = count(t)

return s_count == t_count


def count(string):
	count_map = defaultdict(int)
	for char in string:
		count_map[char] += 1
	return count_map


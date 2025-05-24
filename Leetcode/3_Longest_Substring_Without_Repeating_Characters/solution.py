# Sliding Window O(n) 

max_length = 0
seen = {}
left = 0
right = 0

if len(s) == 0:
	return 0

while right < len(s):
	cur_char = s[right]
	if cur_char in seen:
		left = max(left, seen[cur_char] + 1)
	seen[cur_char] = right
	substring_len = (right - left) + 1
	max_length = max(substring_len, max_length)
	right += 1

return max_length



[ABABC] k=2
4

[ACABCABBBA] k=1
3

# Sliding Window O(n)

max_len = 0
counts = defaultdict(int) 

left = 0
max_occurred = 0
for right in range(len(s)):
	
	counts[s[r]] += 1
	max_occurred = max(max_occurred, counts[s[r]])
	
	while (r - l + 1) - max_occurred > k:
		counts[s[l]] -= 1
		l += 1

	max_len = max(max_len, (r - l + 1))
return max_len



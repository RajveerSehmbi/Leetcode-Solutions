# Hash Set O(n)

num_set = set(nums)
longest_sequence = 0

for num in num_set:
	if num-1 not in num_set:
		seq = 0
		cur = num
		while cur in num_set:
			seq += 1
			cur += 1
		longest_sequence = max(seq, longest_sequence)
return longest_sequence

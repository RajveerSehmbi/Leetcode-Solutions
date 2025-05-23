# Brute Force O(n^2)

for i in range(nums):
	for j in range(nums):
		if j == i:
			continue
		if nums[i] + nums[j] == target:
			return [i, j]
return []




# One-pass HashMap O(n)

seen = {}
for i in range(len(nums)):
	num = nums[i]
	difference = target - num
	if difference in seen:
		return [i, seen[difference]]
	seen[num] = i
return []

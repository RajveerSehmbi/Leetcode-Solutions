# Brute Force O(n^2)

n = len(nums)
for i in range(nums):
	for j in range(i, nums):
		if nums[j] == nums[i]:
			return True
return False



# Optimal O(n)

seen = set()
for num in nums:
	if num in seen:
		return True
	seen.add(num)
return False


# Example Cases
[1,2,3,4]
[1,2,1,3]


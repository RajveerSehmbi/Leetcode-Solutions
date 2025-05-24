# Brute force O(N^3)




# Two pointer O(n^2)

nums.sort()
res = []
n = len(nums)

for i in range(n-2):
	if nums[i] > 0:
		break

	if i > 0 and nums[i] == nums[i-1]:
		continue

	target = 0 - nums[i]
	left = i + 1
	right = n - 1
	while left < right:
		left_num = nums[left]
		right_num = nums[right]
		pair_sum = left_num + right_num		

		if pair_sum == target:
			res.append([nums[i], nums[left], nums[right]])
			while left < n and nums[left] == left_num:
				left += 1
			while right > -1 and nums[right] == right_num:
				right -= 1
		elif pair_sum < target:
			left += 1
		else:
			right -=1
return res
	

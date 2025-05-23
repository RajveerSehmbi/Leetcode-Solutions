# Brute Force O(n^2)

n = len(nums)
res = [1] * n
for i in range(n):
	for j in range(n):
		if i == j:
			continue
		res[i] *= nums[j]
return res




# 

n = len(nums)
pre_product = [1] * n
for i in range(1, n):
	pre_product[i] = nums[i-1] * pre_product[i-1]

post_product = [1] * n
for j in range(n-2, -1, -1):
	post_product[j] = nums[j+1] * post_product[j+1]

res = [1] * n
for k in range(n):
	res[k] *= pre_product[k] * post_product[k]
return res	
	

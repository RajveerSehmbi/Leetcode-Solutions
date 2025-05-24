# Two Pointer O(n)

max_area = 0
left = 0
right = len(height) - 1

while left < right:

	cur_area = None
	if height[left] <= height[right]:
		cur_area = height[left] * (right - left)
		left += 1
	else:
		cur_area = height[right] * (right - left)
		right -= 1
	
	max_area = max(max_area, cur_area)

return max_area


# Sorting 
# O(m) for addNum
# O(m * nlogn) for findMedian

class MedianFinder:
	
	def __init__(self):
		self.data = []

	def addNum(self, num):
		self.data.append(num)
	
	def findMedian(self):
		self.data.sort()    # O(nlogn)
		n = len(self.data)
		l_mid_idx = (n - 1)/2
		if n & 1:
			return self.data[n // 2]
		return  self.data[n // 2 - 1] + self.data[n // 2]) / 2
		



# Heap

class MedianFinder:
	
	def __init__(self):
		self.small = []   # max heap
		self.large = []   # min heap

	def addNum(self, num):
		if self.large and num > self.large[0]:
			heapq.heappush(self.large, num)
		else:
			heapq.heappush(self.small, -1 * num)
		
		if len(self.small) > len(self.large) + 1:
			val = -1 * heapq.heappop(self.small)
			heapq.heappush(self.large, val)
		if len(self.large) > len(self.small) + 1:
			val = heapq.heappop(self.large)
			heapq.heappush(self.small, -1 * val)

	def findMedian(self):
		if len(self.small) > len(self.large):
			return -1 * self.small[0]
		elif len(self.large) > len(self.small):
			return self.large[0]
		return (-1 * self.small[0] + self.large[0]) / 2.0

# Hashmap O(n)

# O(n)
count = defaultdict(int)
for num in nums:
	count[num] += 1

# O(n)
freq = defaultdict(list)
for num, count in count.items():
	freq[count].append(num)

# O(n)
res = []
for i in range(len(nums)+1):
	if i in freq:
		res.extend(freq[i])
return res[-k:]






# Min-heap O(nlogk)
# k is the number of heap elements

count = defaultdict(int)
for num in nums:
	count[num] += 1

heap = []
for num, cnt in count.items():
	heapq.heappush(heap, (cnt, num))
	if len(heap) > k:
		heapq.heappop(heap)

res = []
for i in range(k):
	res.append(heapq.heappop(heap)[1])
return res


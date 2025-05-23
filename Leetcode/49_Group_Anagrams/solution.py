# Sort O(m * nlogn)
# m is the number of words
# n is the size of the longest word

anagram_groups = defaultdict(list)
for word in strs:
	sorted_word = ''.join(sorted(word))   # O(nlogn)
	anagram_groups[sorted_word].append(word)
return list(anagram_groups.values())





# Hashing O(mn)

anagram_groups = defaultdict(list)
for word in strs:
	count = [0] * 26
	word = word.lower()    # not needed if string is already lowercase
	for char in word:
		count[ord(char) - ord('a')] += 1
	anagram_groups[tuple(count)].append(word)
return list(anagram_groups.values())

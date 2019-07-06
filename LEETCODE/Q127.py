class Solution(object):
	# @param start, a string
	# @param end, a string
	# @param dict, a set of string
	# @return an integer
	def ladderLength(self, start, end, dicti):
		dicti.add(end)
		q = []
		q.append((start, 1))  #(['hit', 1])
		while q:
			current = q.pop(0)
			currentWord = current[0]; currentlen = current[1]
			if(currentWord == end): return currentlen
			for i in range(len(start)):
				part1 = currentWord[:i]; part2 = currentWord[i+1:]
				print(part1,part2)
				for j in 'abcdefghijklmnopqrstuvwxyz':
					if(currentWord[i]!=j):
						nextword = part1 + j+ part2
						if nextword in dicti:
							q.append((nextword, currentlen+1))
							dicti.remove(nextword)
		return 0

beginWord = 'hit'
endWord = 'cog'
wordList = set(["hot","dot","dog","lot","log","cog"])
print(Solution().ladderLength(beginWord, endWord, wordList))
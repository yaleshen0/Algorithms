'''
Time complexity: O(n2)
'''

def lengthOfLongestSubstring(s):
#     """
#     :type s: str
#     :rtype: int
#     """
    max_len = 0
    for i in range(len(s)):
        # print(helper(s,i))
        max_len = max(max_len, helper(s, i))
    return max_len
        
def helper(s, starting_index):
    # print(starting_index)
    seen = set()
    for i in range(starting_index, len(s)):
        if s[i] not in seen:
            seen.add(s[i])
        else:
            return i - starting_index
    print(len(s), starting_index, len(s)-starting_index)
    return len(s) - starting_index

print(lengthOfLongestSubstring('pwwkew'))


#------------------------------------------------------------
''' Sliding window
Time complexity: O(n)
'''

def longest_substring_without_repeat(s):
    seen = {}
    max_len = 0
    start = 0
    for end in range(len(s)):
        if s[end] in seen:
            start = max(start, seen[s[end]] + 1)
        seen[s[end]] = end
        max_len = max(max_len, end - start + 1)
    return max_len

print(longest_substring_without_repeat('pwwkew'))


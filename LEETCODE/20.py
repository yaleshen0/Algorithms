# Example 1:
# Input: "()"
# Output: true
# Example 2:
# Input: "()[]{}"
# Output: true
# Example 3:
# Input: "(]"
# Output: false
# Example 4:
# Input: "([)]"
# Output: false
# Example 5:
# Input: "{[]}"
# Output: true
# class Solution(object):
#     def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # bracket_mapping ={"(": ")", "[": "]", "{" :"}"}
        # open_bracket = []
        # if not s: return True
        # # if s[0] in bracket_mapping.values():
        # #     return False
        # for i in s:
        #     if (i == "("): open_bracket.append("(")
        #     elif (i == "["): open_bracket.append("[")
        #     elif(i == "{"): open_bracket.append("{")
        #     else:
        #         if (len(open_bracket) == 0): return False
        #         elif (bracket_mapping[open_bracket[-1]] == i):
        #             open_bracket.pop()
        #         else:
        #             return False
        # return len(open_bracket) == 0
 class Solution(object):
    def isValid(self, s):
        open_bracket = []
        for i in s:
            if (i == "("): open_bracket.append(")")
            elif (i == "["): open_bracket.append("]")
            elif(i == "{"): open_bracket.append("}")
            else:
                if (len(open_bracket) == 0): return False
                elif (open_bracket[-1] != i): return False
                open_bracket.pop()
        return len(open_bracket) == 0
# print(Solution().isValid("]()"))
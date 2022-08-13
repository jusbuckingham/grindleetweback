# Easy

# Write a function to find the longest common prefix string amongst 
# an array of strings.

# If there is no common prefix, return an empty string "".

# Example:

# Input: strs = ["flower","flow","flight"]
# Output: "fl"

class Solution:
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        min_s = min(strs)
        max_s = max(strs)
        if not min_s:
            return ""
        for i in range(len(min_s)):
            if max_s[i] != min_s[i]:
                return max_s[:i]
        return min_s[:]
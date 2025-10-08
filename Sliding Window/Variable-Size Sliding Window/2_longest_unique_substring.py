# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        visitedArr = [False] * 128 
        i = 0
        n = len(s)
        maxLen = 0
        
        for j in range(n):
            ch = s[j]
            index = ord(ch)
            
            while visitedArr[index]:  
                visitedArr[ord(s[i])] = False
                i += 1
            
            visitedArr[index] = True
            maxLen = max(maxLen, j - i + 1)
        
        return maxLen

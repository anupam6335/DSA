# Word Pattern — #290
# problem link : https://leetcode.com/problems/word-pattern/description/

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        n = len(pattern)
        words = s.split()
        m = len(words)
        if n != m:
            return False
        
        map_pattern = {}
        map_s = {}
        for pat, st in zip(pattern, words):
            if pat in map_pattern and map_pattern[pat] != st:
                return False
            if st in map_s and map_s[st] != pat:
                return False
            map_pattern[pat] = st
            map_s[st] = pat
        
        return True

sol = Solution()
print(sol.wordPattern("aaa", "aa aa aa aa"))
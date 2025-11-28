# Valid anagram (LC 242)
# Question Link : https://leetcode.com/problems/valid-anagram/

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # return sorted(s) == sorted(t) # Sol 1

        dict_s = {}
        dict_t = {}
        for ch in s:
            dict_s[ch] = dict_s.get(ch, 0) + 1
        for ch in t:
            dict_t[ch] = dict_t.get(ch, 0) + 1
        
        return dict_s == dict_t
       
        
sol = Solution()
print(sol.isAnagram("ab", "a"))
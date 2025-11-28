# Group anagrams (LC 49)
# Question Link : https://leetcode.com/problems/group-anagrams/description/

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        dict_strs = {}

        for ch in strs:
            sorted_ch = ''.join(sorted(ch))
            if sorted_ch not in dict_strs:
                dict_strs[sorted_ch] = []
            dict_strs[sorted_ch].append(ch)
        return list(dict_strs.values())
        # res = []
        # for ch in dict_strs.values():
        #     res.append(ch)
        # return res
        
""" 

SHORTER VERSION 
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        for word in strs:
            key = ''.join(sorted(word))
            groups[key].append(word)

        return list(groups.values())


 """

sol = Solution()
print(sol.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
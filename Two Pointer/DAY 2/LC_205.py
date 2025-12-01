# Isomorphic Strings — #205
# Problem Link : https://leetcode.com/problems/isomorphic-strings/


# class Solution:
#     def isIsomorphic(self, s: str, t: str) -> bool:
#         n = len(s)
#         m = len(t)
#         if n != m:
#             return False
#         mapping = {}
#         reverse_map = {} 
#         i = 0
#         while i < n:
#             c1 = s[i]
#             c2 = t[i]
#             if c1 in mapping and mapping[c1] != c2:
#                 return False
#             if c2 in reverse_map and reverse_map[c2] != c1:
#                 return False
        
#             mapping[c1] = c2
#             reverse_map[c2] = c1
#             i += 1
#         return True
    
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        map_s={}
        map_t={}

        for sc,tc in zip(s,t):
            if sc in map_s and map_s[sc] !=tc:
                return False
            if tc in map_t and map_t[tc] !=sc:
                return False

            map_s[sc]= tc
            map_t[tc]= sc
        return True       

sol = Solution()
print(sol.isIsomorphic("badc", "baba"))
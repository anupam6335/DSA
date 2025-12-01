# Intersection of Two Arrays — #349
# problem Link : https://leetcode.com/problems/intersection-of-two-arrays/description/


class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        seen = {}

        for n in nums1:
            if n not in seen:
                seen[n] = True 
        
        res = []

        for n in nums2:
            if n in seen:
                res.append(n)
                del seen[n]
        return res


sol = Solution()
print(sol.intersection([1,2,2,1], [2,2]))
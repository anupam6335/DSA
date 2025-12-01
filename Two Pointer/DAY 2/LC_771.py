# Jewels and Stones — #771
# Problems Link : https://leetcode.com/problems/jewels-and-stones/

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        cnt = 0

        for st in stones:
            if st in jewels:
                cnt += 1
        return cnt

sol = Solution()
print(sol.numJewelsInStones("aA","aAAbbbb"))
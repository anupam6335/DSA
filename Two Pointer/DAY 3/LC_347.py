# Top K Frequent Elements — #347
# problem link : https://leetcode.com/problems/top-k-frequent-elements/description/ 


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}

        for n in nums:
            freq[n] = freq.get(n, 0) + 1

        # Sort by frequency descending
        sorted_items = sorted(freq.items(), key=lambda x: x[1], reverse=True)

        # Take the top k keys (the numbers)
        res = [key for key, val in sorted_items[:k]]
        return res
 

sol  = Solution()
print(sol.topKFrequent([1,1,1,2,2,3], 2))
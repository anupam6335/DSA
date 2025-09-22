# https://leetcode.com/problems/k-radius-subarray-averages/

class Solution:
    def getAverages(self, nums: list[int], k: int) -> list[int]:
        n = len(nums)
        window_size = 2 * k + 1
        i = 0
        curr_sum = 0

        res = [-1]*n

        for j in range(n):
            curr_sum += nums[j]
            if j - i + 1 == window_size:
                mid = i + k

                res[mid] = curr_sum // window_size
                curr_sum -= nums[i]
                i += 1
        return res 


sol = Solution()
print(sol.getAverages([7,4,3,9,1,8,5,2,6], 3))
        
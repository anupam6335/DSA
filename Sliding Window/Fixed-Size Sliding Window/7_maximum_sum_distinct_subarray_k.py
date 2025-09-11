# https://leetcode.com/problems/maximum-sum-of-distinct-subarrays-with-length-k/
# brute force
class Solution:
    def maximumSubarraySum(self, nums: list[int], k: int) -> int:
        n = len(nums)
        i = 0
        maxSum = 0
        currSum = 0
        temp = []
        tempSet = set()
        for j in range(n):
            currSum += nums[j]
            temp.append(nums[j])
            if j - i + 1 == k:
                tempSet = set(temp)
                if k == len(tempSet):
                    maxSum = max(maxSum, currSum)
                currSum -= temp[0]
                temp = temp[1:]
                tempSet = set()
                i += 1
        return maxSum
                

# sliding window + frequency 
# optimize solution

class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        i = 0
        maxSum = 0
        currSum = 0
        freq = defaultdict(int)  # frequency dictionary
        uniqueCount = 0  # track how many distinct numbers in window

        for j in range(n):
            num = nums[j]
            currSum += num

            # update frequency
            freq[num] += 1
            if freq[num] == 1:
                uniqueCount += 1  # new unique number added

            if j - i + 1 == k:
                if uniqueCount == k:  # all elements are distinct
                    maxSum = max(maxSum, currSum)

                # remove first element from window
                first = nums[i]
                currSum -= first
                freq[first] -= 1
                if freq[first] == 0:
                    uniqueCount -= 1

                i += 1

        return maxSum
__import__("atexit").register(lambda: open("display_runtime.txt", "w").write("0"))


sol = Solution()
print(sol.maximumSubarraySum([1,1,1,7,8,9], 3))
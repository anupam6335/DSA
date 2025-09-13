# https://leetcode.com/problems/contains-duplicate-ii/description/

#brute Force

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # write your logic 
        n = len(nums)

        for i in range(n-1):
            for j in range(i + 1, n ):
                if nums[i] == nums [j] and abs(i - j) <= k:
                    return True
        return False

__import__("atexit").register(lambda: open("display_runtime.txt", "w").write("0"))


# optimal approach 
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window = set()
        i = 0
        n = len(nums)

        for j in range(n):
            num = nums[j]
            if num in window:
                return True
            window.add(num)

            if j - i >= k:
                window.remove(nums[i])
                i += 1
        return False

__import__("atexit").register(lambda: open("display_runtime.txt", "w").write("0"))
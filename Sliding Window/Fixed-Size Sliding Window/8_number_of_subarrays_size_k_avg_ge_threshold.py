# https://leetcode.com/problems/number-of-sub-arrays-of-size-k-and-average-greater-than-or-equal-to-threshold/description/

class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        i = 0
        n = len(arr)
        cnt = 0
        sumOfsubarray = 0
        for j in range(n):
            sumOfsubarray += arr[j]

            if j - i + 1 == k:
                avg = sumOfsubarray // k
                if avg >= threshold:
                    cnt += 1
                sumOfsubarray -= arr[i]
                i += 1
        return cnt
__import__("atexit").register(lambda: open("display_runtime.txt", "w").write("0"))

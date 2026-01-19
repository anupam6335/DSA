# problem link : https://www.geeksforgeeks.org/problems/count-triplets-with-sum-smaller-than-x5549/1
class Solution:
    def countTriplets(self, n, sum, arr):
        arr.sort()
        cnt = 0
        n = len(arr)

        for k in range(n - 2):
            i = k + 1
            j = n - 1

            while i < j:
                curr_sum = arr[k] + arr[i] + arr[j]

                if curr_sum >= sum:
                    j -= 1
                else:
                    cnt += (j - i)
                    i += 1

        return cnt


# ----------- MAIN CODE -----------
if __name__ == "__main__":
    t = int(input().strip())   # number of test cases
    for _ in range(t):
        n, sum_val = map(int, input().split())
        arr = list(map(int, input().split()))

        obj = Solution()
        print(obj.countTriplets(n, sum_val, arr))

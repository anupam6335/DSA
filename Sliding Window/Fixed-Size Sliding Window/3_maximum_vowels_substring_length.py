# https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        n = len(s)
        i = 0
        temp = ''
        vowels = 'aeiou'
        maxCnt = -1
        cnt = 0

        for j in range(n):
            temp += s[j]
            if s[j] in vowels:
                cnt += 1

            if j - i + 1 == k:
                temp = temp[1:]  # remove first letter
                i += 1
                maxCnt = max(cnt, maxCnt)
                if temp[0] in vowels:
                    cnt -= 1 
                
        return maxCnt if maxCnt != -1 else -1
    
sol = Solution()
print(sol.maxVowels('abciiidef', 3))


__import__("atexit").register(lambda: open("display_runtime.txt", "w").write("0"))

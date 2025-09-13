# https://www.geeksforgeeks.org/problems/count-occurences-of-anagrams5839/1 ( brute force not work here showing wrong output)
# brute force approach 

""" class Solution:

	
	def search(self,pat, txt):
	    # code here
	    n = len(pat)
	    m = len(txt)
	    cnt = 0
	    for i in range(n):
	        newStr = pat[i : i + m]
	        if sorted(newStr) == sorted(txt):
	            cnt += 1
	    return cnt
 """

 
#User function Template for python3
from collections import Counter

class Solution:

	
	def search(self,pat, txt):
	    # code here
	    n, m = len(txt), len(pat)
	    cnt = 0
	    pat_count = Counter(pat)
	    txt_count = Counter(txt[:m])
	    if pat_count == txt_count:
	        cnt += 1
	    for i in range(m, n):
	        txt_count[txt[i]] += 1
	        txt_count[txt[i - m]] -=1
	        
	        if txt_count[txt[i - m]] == 0:
	            del txt_count[txt[i - m]]
	       
	        if pat_count == txt_count:
	            cnt += 1
	    return cnt



# https://leetcode.com/problems/find-all-anagrams-in-a-string/description/
#
from collections import Counter

class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        n, m = len(s), len(p)
        if m > n:
            return []
        
        p_count = Counter(p)             # frequency count of p
        window_count = Counter(s[:m])    # first window
        res = []
        
        if window_count == p_count:
            res.append(0)
        
        # sliding window
        for i in range(m, n):
            window_count[s[i]] += 1            # add new char
            window_count[s[i - m]] -= 1        # remove old char
            if window_count[s[i - m]] == 0:    # cleanup to keep dict small
                del window_count[s[i - m]]
            
            if window_count == p_count:
                res.append(i - m + 1)
        
        return res

sol = Solution()
print(sol.findAnagrams('aabaabaa', 'aaba'))
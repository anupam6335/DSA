# https://www.geeksforgeeks.org/problems/count-distinct-elements-in-every-window/1

# brute force approach 
class Solution:
    def countDistinct(self, arr, k):
        # keep your window logic; just fix the counting
        res, temp = [], []
        i, n = 0, len(arr)

        if k <= 0 or k > n:
            return []

        for j in range(n):
            temp.append(arr[j])

            if j - i + 1 == k:
                # count distinct in this window
                res.append(len(set(temp)))

                # slide window by one (keep your approach)
                temp = temp[1:]
                i += 1

        return res




# Optimize solution 

class Solution:
    def countDistinct(self, arr, k):
        n = len(arr)
        if k <= 0 or k > n:
            return []
        
        freq = {}
        distinct = 0
        res = []
        
        # Initialize the first window [0, k-1]
        for i in range(k):
            num = arr[i]
            if num not in freq:
                freq[num] = 1  # Set directly to 1
                distinct += 1
            else:
                freq[num] += 1
        res.append(distinct)
        
        # Slide the window from [1, k] to [n-k, n-1]
        for i in range(k, n):
            left_num = arr[i - k]   # element to remove
            right_num = arr[i]       # element to add
            
            # Remove left_num
            freq[left_num] -= 1
            if freq[left_num] == 0:
                distinct -= 1
                
            # Add right_num
            if right_num not in freq or freq[right_num] == 0:
                distinct += 1
                freq[right_num] = 1  # Set directly to 1
            else:
                freq[right_num] += 1
            
            res.append(distinct)
            
        return res
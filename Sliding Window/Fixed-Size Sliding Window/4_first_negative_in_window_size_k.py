# Question : https://www.geeksforgeeks.org/problems/first-negative-integer-in-every-window-of-size-k3345/1
# brute force approach 
""" 
class Solution:
    def firstNegInt(self, arr, k):
        i = 0
        temp = []
        res = []
        n = len(arr)

        for j in range(n):
            temp.append(arr[j])
            if j - i + 1 == k:
                cnt = True 
                for num in temp:
                    if num < 0:
                        res.append(num)
                        cnt = False
                        break
                if cnt:
                    res.append(0)
                temp = temp[1:]
                i += 1
        return res """
class Solution:
    def firstNegInt(self, arr, k):
        neg_list = []
        res = []
        n = len(arr)
        i = 0
        for j in range(n):
            # Remove indices that are out of the current window from the beginning of neg_list
            while neg_list and neg_list[0] < i:
                neg_list.pop(0)
            
            if arr[j] < 0:
                neg_list.append(j)
                
            if j - i + 1 == k:
                if neg_list:
                    res.append(arr[neg_list[0]])
                else:
                    res.append(0)
                i += 1
        return res

# Example run
sol = Solution()
print(sol.firstNegInt([-8, -2, -3, -6, -10, -2,-2,-3,-4], 2))



""" 
 Here are the key concepts to remember from this code that you can apply to future sliding window problems:

### 1. **Sliding Window Pattern**
- Use two pointers: `i` (window start) and `j` (window end)
- Expand window by moving `j` forward
- Shrink window by moving `i` forward when window size reaches `k`

### 2. **Data Structure for Tracking Elements**
- Use a list/deque to track **indices** (not values) of important elements
- In this case: track indices of negative numbers
- Can be adapted for: maximum/minimum values, specific conditions, etc.

### 3. **Maintaining Relevance**
```python
while neg_list and neg_list[0] < i:
    neg_list.pop(0)
```
- **Key Concept**: Remove elements that are no longer in the current window
- Always check if tracked indices are still within window bounds
- This ensures your data structure only contains relevant information

### 4. **Efficient Checking**
- Instead of scanning entire window each time, use the tracked data structure
- First element in your tracking list represents the desired element (here: first negative)
- Time complexity improves from O(n*k) to O(n)

### 5. **Window Size Check**
```python
if j - i + 1 == k:
```
- Standard formula to check if current window has reached size `k`
- Universal for all sliding window problems

### 6. **Edge Case Handling**
```python
if neg_list:
    res.append(arr[neg_list[0]])
else:
    res.append(0)
```
- Always consider what happens when no element meets your condition
- Provide appropriate default value

## When to Apply This Pattern

Use this approach when you need to:
- Find first/last occurrence of something in each window
- Track maximum/minimum values in sliding windows  
- Count specific elements in each window
- Any problem where you need to avoid rescanning the entire window

## Template for Future Problems

```python
def sliding_window(arr, k):
    tracker = []  # stores indices of important elements
    result = []
    i = 0  # window start
    
    for j in range(len(arr)):  # j = window end
        # Remove outdated indices
        while tracker and tracker[0] < i:
            tracker.pop(0)
        
        # Add current element if it meets condition
        if condition(arr[j]):
            tracker.append(j)
        
        # Process when window is full
        if j - i + 1 == k:
            if tracker:
                result.append(process(arr[tracker[0]]))
            else:
                result.append(default_value)
            i += 1  # slide window
    
    return result
```

Remember: The core idea is to **track indices, not values**, and **maintain relevance** by removing outdated indices!


 """

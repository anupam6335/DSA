# problem link : https://leetcode.com/problems/two-sum-iv-input-is-a-bst/description/


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        nums = []
        
        def inorder(root):
            if not root:
                return
            inorder(root.left)
            nums.append(root.val)
            inorder(root.right)
        
        inorder(root)
        
        i = 0
        j = len(nums) - 1
        
        while i < j:
            curr_sum = nums[i] + nums[j]
            if curr_sum < k:
                i += 1
            elif curr_sum > k:
                j -= 1
            else:
                return True
        return False

# -------------------------
# Example usage / main
# -------------------------
if __name__ == "__main__":
    # Create a sample tree:
    #       5
    #      / \
    #     3   6
    #    / \   \
    #   2   4   7
    root = TreeNode(5)
    root.left = TreeNode(3, TreeNode(2), TreeNode(4))
    root.right = TreeNode(6, None, TreeNode(7))
    
    k = 9  # target sum
    
    solution = Solution()
    result = solution.findTarget(root, k)
    print("Result:", result)

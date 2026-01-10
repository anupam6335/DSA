# problem Link : https://neetcode.io/problems/lowest-common-ancestor-of-a-binary-tree-iii/question?list=allNC
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None


class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        a, b = p, q
        while a != b:
            a = a.parent if a else q
            b = b.parent if b else p
        return a


# ---- Example Run ----
if __name__ == "__main__":
    # Build tree
    root = Node(3)
    n5 = Node(5)
    n1 = Node(1)
    n6 = Node(6)
    n2 = Node(2)

    root.left = n5
    root.right = n1
    n5.left = n6
    n5.right = n2

    n5.parent = root
    n1.parent = root
    n6.parent = n5
    n2.parent = n5

    sol = Solution()
    lca = sol.lowestCommonAncestor(n6, n2)
    print(lca.val)  # Output: 5

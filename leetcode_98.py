# Validate Binary Search Tree

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def buildFromList(self, lst):  # [1,null,2,3]
        if not lst:
            return None
        else:
            val = lst.pop(0)
            root = TreeNode(val)
            queue = [root]
            while lst and queue:
                node = queue.pop(0)
                val = lst.pop(0)
                if val != 'null':
                    anode = TreeNode(val)
                    node.left = anode
                    queue.append(anode)
                else:
                    node.left = None
                if lst:
                    val = lst.pop(0)
                    if val != 'null':
                        anode = TreeNode(val)
                        node.right = anode
                        queue.append(anode)
                    else:
                        node.right = None
            return root


# Validate Binary Search Tree
class Solution:
    def isValidBST(self, root: [TreeNode]) -> bool:

        def isValid(node: [TreeNode], lowerLimit, upperLimit):
            if not node:
                return True
            else:
                return lowerLimit < node.val < upperLimit and isValid(node.left, lowerLimit, node.val) and isValid(
                    node.right, node.val, upperLimit)

        inf = (2 ** 31) + 1  # -2^31 <= Node.val <= 2^31 - 1
        return isValid(root, -inf, inf)


T = TreeNode()
root = T.buildFromList([8, 5, 9, 3, 6, 7, 10])
s = Solution()
print(s.isValidBST(root))

T = TreeNode()
root = T.buildFromList([5, 4, 6, 'null', 'null', 3, 7])
s = Solution()
print(s.isValidBST(root))

T = TreeNode()
root = T.buildFromList([2])
s = Solution()
print(s.isValidBST(root))

T = TreeNode()
root = T.buildFromList([2, 1])
s = Solution()
print(s.isValidBST(root))

T = TreeNode()
root = T.buildFromList([2, 'null', 3])
s = Solution()
print(s.isValidBST(root))

T = TreeNode()
root = T.buildFromList([2, 1, 3])
s = Solution()
print(s.isValidBST(root))

T = TreeNode()
root = T.buildFromList([5, 1, 4, 'null', 'null', 3, 6])
s = Solution()
print(s.isValidBST(root))

T = TreeNode()
root = T.buildFromList([1, 'null', 1])
s = Solution()
print(s.isValidBST(root))

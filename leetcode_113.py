# Path Sum II

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


# Path Sum II
class Solution:
    def pathSum(self, root: [TreeNode], targetSum: int) -> bool:
        res = []

        def backtrack(node, current):
            if node and not node.left and not node.right:
                current.append(node.val)
                if sum(current) == targetSum:
                    res.append(current)
                else:
                    return
            else:
                candidate_list = []
                if node.left:
                    candidate_list.append(node.left)
                if node.right:
                    candidate_list.append(node.right)
                for candidate in candidate_list:
                    backtrack(candidate, current + [node.val])

        if not root:
            return res
        else:
            backtrack(root, [])

        return res


T = TreeNode()
root = T.buildFromList([5, 4, 8, 11, 'null', 13, 4, 7, 2, 'null', 'null', 5, 1])
s = Solution()
print(s.pathSum(root, targetSum=22))

T = TreeNode()
root = T.buildFromList([5, 4, 8, 11, 'null', 13, 4, 7, 2, 'null', 'null', 'null', 1])
s = Solution()
print(s.pathSum(root, targetSum=22))

print(s.pathSum(root, targetSum=26))

print(s.pathSum(root, targetSum=27))

print(s.pathSum(root, targetSum=18))

print(s.pathSum(root, targetSum=11))

T = TreeNode()
root = T.buildFromList([1, 2, 3])
s = Solution()
print(s.pathSum(root, targetSum=5))

T = TreeNode()
root = T.buildFromList([1, 2])
s = Solution()
print(s.pathSum(root, targetSum=0))

T = TreeNode()
root = T.buildFromList([])
s = Solution()
print(s.pathSum(root, targetSum=5))

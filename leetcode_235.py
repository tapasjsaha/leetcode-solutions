# Lowest Common Ancestor of a Binary Search Tree

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


# Lowest Common Ancestor of a Binary Search Tree
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        currNode = root
        x = min(p.val, q.val)
        y = max(p.val, q.val)
        # p and q will exist in the BST -> this condition makes it easy and ensure the last else is the result
        while True:
            if y < currNode.val:
                currNode = currNode.left
            elif x > currNode.val:
                currNode = currNode.right
            else:
                return currNode


T = TreeNode()
root = T.buildFromList([5, 3, 6, 2, 4, 'null', 7])
p = TreeNode(2)
q = TreeNode(8)
s = Solution()
print(s.lowestCommonAncestor(root, p, q))


# Search in a Binary Search Tree

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

# Search in a Binary Search Tree
class Solution:
    def searchBST(self, root: [TreeNode], val: int) -> [TreeNode]:
        currNode = root
        while currNode:
            if val == currNode.val:
                return currNode
            elif val < currNode.val and currNode.left:
                currNode = currNode.left
            elif val > currNode.val and currNode.right:
                currNode = currNode.right
            else:
                return None


T = TreeNode()
root = T.buildFromList([4, 2, 7, 1, 3])
s = Solution()
print(s.searchBST(root, val=4))

T = TreeNode()
root = T.buildFromList([4, 2, 7, 1, 3])
s = Solution()
print(s.searchBST(root, val=2))

T = TreeNode()
root = T.buildFromList([4, 2, 7, 1, 3])
s = Solution()
print(s.searchBST(root, val=5))

T = TreeNode()
root = T.buildFromList([62, 2, 93, 'null', 30, 'null', 'null', 15, 'null', 'null', 'null'])
s = Solution()
print(s.searchBST(root, val=15))

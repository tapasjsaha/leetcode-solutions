# Insert into a Binary Search Tree

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


# Insert into a Binary Search Tree
class Solution:
    def insertIntoBST(self, root: [TreeNode], val: int) -> [TreeNode]:
        newNode = TreeNode(val)
        if not root:
            root = newNode
        else:
            currNode = root
            while True:
                if val < currNode.val and currNode.left:
                    currNode = currNode.left
                elif val > currNode.val and currNode.right:
                    currNode = currNode.right
                else:
                    if val < currNode.val and not currNode.left:
                        currNode.left = newNode
                        break
                    elif val > currNode.val and not currNode.right:
                        currNode.right = newNode
                        break
        return root


T = TreeNode()
root = T.buildFromList([4, 2, 7, 1, 3])
s = Solution()
print(s.insertIntoBST(root, val=5))

T = TreeNode()
root = T.buildFromList([40, 20, 60, 10, 30, 50, 70])
s = Solution()
print(s.insertIntoBST(root, val=25))

T = TreeNode()
root = T.buildFromList([4, 2, 7, 1, 3])
s = Solution()
print(s.insertIntoBST(root, val=5))

# Unique Binary Search Trees II

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Not required for this problem
#    def buildFromList(self, lst):  # [1,null,2,3]
#        if not lst:
#            return None
#        else:
#            val = lst.pop(0)
#            root = TreeNode(val)
#            queue = [root]
#            while lst and queue:
#                node = queue.pop(0)
#                val = lst.pop(0)
#                if val != 'null':
#                    anode = TreeNode(val)
#                    node.left = anode
#                    queue.append(anode)
#                else:
#                    node.left = None
#                if lst:
#                    val = lst.pop(0)
#                    if val != 'null':
#                        anode = TreeNode(val)
#                        node.right = anode
#                        queue.append(anode)
#                    else:
#                        node.right = None
#            return root

    def printTree(self, root):
        res = []
        if root:
            queue = [root]
            while queue:
                node = queue.pop(0)
                if node:
                    res.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)
                else:
                    res.append('null')
            while res[-1] == 'null':
                res.pop()
        return res


# Unique Binary Search Trees II

class Solution:
    def generateTrees(self, n: int) -> [[]]:

        def createTree(start, end):
            if start > end:
                return [None]
            else:
                all_trees = []
                for current in range(start, end+1):
                    all_left_trees = createTree(start, current-1)
                    all_right_trees = createTree(current + 1, end)

                    for left_tree in all_left_trees:
                        for right_tree in all_right_trees:
                            rootNode = TreeNode(val=current)
                            rootNode.left = left_tree
                            rootNode.right = right_tree
                            all_trees.append(rootNode)
                return all_trees

        return createTree(1, n)


T = TreeNode()
s = Solution()
res = s.generateTrees(n=3)

for treeRoot in res:
    print(T.printTree(treeRoot))



# Lowest Common Ancestor of a Binary Tree
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None
        elif root == p or root == q:  # LCA is this node as other node is descendant of this node
            return root
        else:
            l = self.lowestCommonAncestor(root.left, p, q)  # consider both the nodes are in left of this node
            r = self.lowestCommonAncestor(root.right, p, q)  # consider both the nodes are in right of this node
            if l and r:
                return root # LCA is this node as two nodes are in left and right of this node
            elif l:
                return l
            else:
                return r


######  Solution 1 - 5.05%
#        inorder_list = []
#
#        def inorder(node):
#            if node.left:
#                inorder(node.left)
#            inorder_list.append(node.val)
#            if node.right:
#                inorder(node.right)
#
#        inorder(root)
#        # node = root
#        while root:
#            ind = inorder_list.index(root.val)
#            if root == p:
#                return root
#            elif root == q:
#                return root
#            elif (p.val in inorder_list[:ind] and q.val not in inorder_list[:ind]) or (p.val not in inorder_list[:ind] and q.val in inorder_list[:ind]):
#                return root
#            elif p.val in inorder_list[:ind] and q.val in inorder_list[:ind]:
#                root = root.left
#            else:
#                root = root.right


#root = [3, 5, 1, 6, 2, 0, 8, null, null, 7, 4]

a = TreeNode(6)
b = TreeNode(7)
c = TreeNode(4)
d = TreeNode(0)
e = TreeNode(8)
f = TreeNode(2, left=b, right=c)
g = TreeNode(5, left=a, right=f)
h = TreeNode(1, left=d, right=e)
root_node = TreeNode(3, left=g, right=h)


s = Solution()
ans = s.lowestCommonAncestor(root_node, g, h)  # 3
print(ans.val)
ans = s.lowestCommonAncestor(root_node, g, c)  # 5
print(ans.val)
ans = s.lowestCommonAncestor(root_node, g, a)  # 5
print(ans.val)
ans = s.lowestCommonAncestor(root_node, d, e)  # 1
print(ans.val)
ans = s.lowestCommonAncestor(root_node, b, c)  # 2
print(ans.val)

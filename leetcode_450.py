# Delete Node in a BST
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BinaryTree:
    def createTree(self, data):
        """Decodes list data to tree.
        :type data: list
        :rtype: TreeNode(root)
        """
        self.i = 0

        def helper(arr, l, ind):
            if arr[ind] == 'null':
                return None
            else:
                node = TreeNode(int(arr[ind]))
                if 2 * ind + 1 < l:
                    node.left = helper(arr, l, 2 * ind + 1)
                if 2 * ind + 2 < l:
                    node.right = helper(arr, l, 2 * ind + 2)
                return node

        if not data:
            return None
        else:
            # inp = data.split('|')
            root = helper(data, len(data), 0)
            return root

    def printTree(self, root):
        """Encodes a tree to a single string.
        :type root: TreeNode
        :rtype: str
        """

        def height(tree_root):
            h = 0
            if tree_root:
                h = 1 + max(height(tree_root.left), height(tree_root.right))
            return h

        def helper(node, ind):
            if node:
                res[ind] = str(node.val)
            if node.left:
                helper(node.left, 2 * ind + 1)
            if node.right:
                helper(node.right, 2 * ind + 2)

        res = []
        if root:
            res = ['null'] * (2 ** height(root) - 1)
            helper(root, 0)
        return ','.join(res)


class Solution:
    def deleteNode(self, root: [TreeNode], key: int) -> [TreeNode]:
        def preorder_successor(node):
            if node.left:
                return preorder_successor(node.left)
            else:
                return node.val

        if not root:
            return None
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
            return root
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
            return root
        else:  #root.val == key
            # there is no child of this node
            if not root.left and not root.right:
                return None
            # there is one child of this node
            elif not root.left:
                return root.right
            elif not root.right:
                return root.left
            # both child of this node is present (replace it with preorder successor)
            else:
                root.val = preorder_successor(root.right)
                root.right = self.deleteNode(root.right, root.val)
                return root




tree = BinaryTree()
root = tree.createTree(data=[5, 3, 6, 2, 4, 'null', 7])
print(root)
print("Hi")  # Debug point to check the Tree
print(tree.printTree(root))

s = Solution()
root = s.deleteNode(root, key=3)
print(tree.printTree(root))

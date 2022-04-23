# Serialize and Deserialize Binary Tree
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.
        :type root: TreeNode
        :rtype: str
        """
        res = []
        def preorder(node):
            if not node:
                res.append('null')
            else:
                res.append(str(node.val))
                preorder(node.left)
                preorder(node.right)

        preorder(root)
        return '|'.join(res)


    def deserialize(self, data):
        """Decodes your encoded data to tree.
        :type data: str
        :rtype: TreeNode
        """
        self.i = 0

        def helper(arr):
            if arr[self.i] == 'null':
                return None
            else:
                node = TreeNode(arr[self.i])
                self.i += 1
                node.left = helper(arr)
                self.i += 1
                node.right = helper(arr)
                return node

        if data == 'null':
            return None
        else:
            inp = data.split('|')
            root = helper(inp)
            return root






# root = [1, 2, 3, 'null', 'null', 4, 5]
#
# root = TreeNode(1)
# b = TreeNode(2)
# c = TreeNode(3)
# d = TreeNode(4)
# e = TreeNode(5)
# f = TreeNode(6)
# root.left = b
# root.right = c
# c.left = d
# c.right = e
# e.right = f
# # print(root)

# Your Codec object will be instantiated and called as such:
ser = Codec()
deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
#ans = ser.serialize(root)
ans = '1|2|null|null|3|4|null|null|5|null|6|null|null'
print(ans)
head=deser.deserialize(ans)
print('Hi')
#ans = deser.deserialize(ser.serialize(root))
ans = ser.serialize(None)

print(ans)
#head=deser.deserialize(ans)
print('Hi')

# Valid solution but applicable for small height trees oly
#
# class Codec:
#     def serialize(self, root):
#         """Encodes a tree to a single string.
#         :type root: TreeNode
#         :rtype: str
#         """
#         def height(tree_root):
#             h = 0
#             if tree_root:
#                 h = 1 + max(height(tree_root.left), height(tree_root.right))
#             return h
#
#         def helper(node, ind):
#             if node:
#                 res[ind] = str(node.val)
#             if node.left:
#                 helper(node.left, 2*ind+1)
#             if node.right:
#                 helper(node.right, 2*ind+2)
#
#         res = []
#         if root:
#             res = ['null'] * (2 ** height(root) - 1)
#             helper(root,0)
#         return '|'.join(res)
#
#
#     def deserialize(self, data):
#         """Decodes your encoded data to tree.
#         :type data: str
#         :rtype: TreeNode
#         """
#         def helper(arr, l, ind):
#             if arr[ind] == 'null':
#                 return None
#             else:
#                 node = TreeNode(int(arr[ind]))
#                 if 2*ind+1 < l:
#                     node.left = helper(arr, l, 2*ind+1)
#                 if 2*ind+2 < l:
#                     node.right = helper(arr, l, 2*ind+2)
#                 return node
#
#         if data:
#             inp = data.split('|')
#             root = helper(inp, len(inp), 0)
#             return root
#         else:
#             return None

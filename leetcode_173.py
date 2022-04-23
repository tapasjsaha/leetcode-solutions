# Binary Search Tree Iterator
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

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

# Binary Search Tree Iterator

class BSTIterator:

    def __init__(self, root: []):
        self.current = 0
        self.iterator = [-1]
        def inOrder(node):
            nodes = []
            if node:
                nodes.extend(inOrder(node.left))
                nodes.append(node.val)
                nodes.extend(inOrder(node.right))
            return nodes
        self.iterator.extend(inOrder(root))

    def hasNext(self) -> bool:
        if self.current+1 >= len(self.iterator):
            return False
        else:
            return True

    def next(self) -> int:
        if self.hasNext():
            self.current += 1
            return self.iterator[self.current]



# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()

T = TreeNode()
root = T.buildFromList([1, 2, 3, 4, 5, 6, 7])
obj = BSTIterator(root)
print(obj.next())
print(obj.hasNext())

print("Hi")
#param_1 = obj.next()
#param_2 = obj.hasNext()

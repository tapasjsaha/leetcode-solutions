# LRU Cache
class ListNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class DoubleLinkList:
    def __init__(self):  # Creating doubly link list
        self.head = None
        self.tail = None

    def insertAtHead(self, key, value):
        node = ListNode(key, value)
        if self.head is None and self.tail is None:  # Empty list
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node
        return node

    def moveToHead(self, node):
        if node.prev is None:                   # First node
            pass
        else:
            if node.next is None:               # last node
                self.tail = node.prev
                node.prev.next = None
            else:                               # Any node in between
                node.next.prev = node.prev
                node.prev.next = node.next
            node.next = self.head
            self.head.prev = node
            node.prev = None
            self.head = node

    def deleteTailNode(self):
        key = self.tail.key
        if self.tail.prev is None:          # Tail node is only node
            self.tail = None
            self.head = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        return key


class LRUCache:
    def __init__(self, capacity: int):
        self.cache = {}
        self.used = DoubleLinkList()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.used.moveToHead(node)
            return node.value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        # Existing key - update
        if key in self.cache:
            # print('Existing key - update')
            node = self.cache[key]
            node.value = value
            self.used.moveToHead(node)
        # New key - insert
        else:
            # Cache already full
            if len(self.cache) == self.capacity:
                # print('Cache already full-Deleting tail node')
                k = self.used.deleteTailNode()
                self.cache.pop(k)

            # print('Inserting new node')
            node = self.used.insertAtHead(key, value)
            self.cache[key] = node


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

# Test case 4:
obj = LRUCache(1)
print(obj.get(6))   # -1
print(obj.get(8))   # -1
obj.put(12, 1)
print(obj.get(2))   # -1
obj.put(15, 11)
obj.put(5, 2)
obj.put(1, 15)
obj.put(4, 2)
print(obj.get(5))   # -1
obj.put(15, 15)



# Test case 3:
obj = LRUCache(10)
obj.put(10, 13)
obj.put(3, 17)
obj.put(6, 11)
obj.put(10, 5)
obj.put(9, 10)
print(obj.get(13))   # -1
obj.put(2, 19)
print(obj.get(2))   # 19
print(obj.get(3))   # 17
obj.put(5, 25)
print(obj.get(8))   # -1
obj.put(9, 22)
obj.put(5, 5)
obj.put(1, 30)
print(obj.get(11))   # -1
obj.put(9, 12)
print(obj.get(7))   # -1
print(obj.get(5))   # 5
print(obj.get(8))   # -1
print(obj.get(9))   # 12
obj.put(4, 30)
obj.put(9, 3)
print(obj.get(9))   # 3
print(obj.get(10))   # 5
print(obj.get(10))   # 5
obj.put(6, 14)
obj.put(3, 1)
print(obj.get(3))   # 1
obj.put(10, 11)
print(obj.get(8))   # -1
obj.put(2, 14)
print(obj.get(1))   # 30
print(obj.get(5))   # 5
print(obj.get(4))   # 30
obj.put(11, 4)
obj.put(12, 24)
obj.put(5, 18)

print(obj.get(13))   # -1
obj.put(7, 23)
print(obj.get(8))   # -1
print(obj.get(12))   # 24
obj.put(3, 27)
obj.put(2, 12)
print(obj.get(5))   # 18
obj.put(2, 9)
obj.put(13, 4)
obj.put(8, 18)
obj.put(1, 7)
print(obj.get(6))   # -1
obj.put(9, 29)
obj.put(8, 21)
print(obj.get(5))   # 18
obj.put(6, 30)
obj.put(1, 12)
print(obj.get(10))   # -1
obj.put(4, 15)
obj.put(7, 22)
obj.put(11, 26)
obj.put(8, 17)
obj.put(9, 29)
print(obj.get(5))   # 18
obj.put(3, 4)
obj.put(11, 30)
print(obj.get(12))   # -1
obj.put(4, 29)
print(obj.get(3))   # 4
print(obj.get(9))   # 29
print(obj.get(6))   # 30
obj.put(3, 4)
print(obj.get(1))   # 12
print(obj.get(10))   # -1
obj.put(3, 29)
obj.put(10, 28)
obj.put(1, 20)
obj.put(11, 13)
print(obj.get(3))   # 29
obj.put(3, 12)
obj.put(3, 8)
obj.put(10, 9)
obj.put(3, 26)
print(obj.get(8))   # 17
print(obj.get(7))   # 22
print(obj.get(5))   # 18
obj.put(13, 17)
obj.put(2, 27)
obj.put(11, 15)
print(obj.get(12))   # -1
obj.put(9, 19)
obj.put(2, 15)
obj.put(3, 16)
print(obj.get(1))   # 20
obj.put(12, 17)
obj.put(9, 1)
obj.put(6, 19)
print(obj.get(4))   # -1
print(obj.get(5))   # 18
print(obj.get(5))   # 18
obj.put(8, 1)
obj.put(11, 7)
obj.put(5, 2)
obj.put(9, 28)
print(obj.get(1))   # 20
obj.put(2, 2)
obj.put(7, 4)
obj.put(4, 22)
obj.put(7, 24)
obj.put(9, 26)
obj.put(13, 28)
obj.put(11, 26)



# Test case 2:
obj = LRUCache(1)
obj.put(2, 1)
print(obj.get(2))
obj.put(3, 2)
print(obj.get(2))
print(obj.get(3))
print("Hi")

# Test case 1:
obj = LRUCache(2)
obj.put(1, 1)
obj.put(2, 2)
print(obj.get(1))
print(obj.get(7))
obj.put(1, 5)
print(obj.get(1))
obj.put(3, 3)
print(obj.get(2))
obj.put(4, 4)
print(obj.get(1))
print(obj.get(3))
print(obj.get(4))


# # LRU Cache 25.27%
# class LRUCache:
#     def __init__(self, capacity: int):
#         from collections import OrderedDict
#         self.cache = OrderedDict()
#         self.capacity = capacity
#
#     def get(self, key: int) -> int:
#         if key in self.cache:
#             self.cache.move_to_end(key)
#             return self.cache[key]
#         else:
#             return -1
#
#     def put(self, key: int, value: int) -> None:
#         if key in self.cache:
#             self.cache[key] = value
#             self.cache.move_to_end(key)
#         else:
#             self.cache[key] = value
#             self.cache.move_to_end(key)
#             if len(self.cache) > self.capacity:
#                 lru = self.cache.popitem(last=False)



# # LRU Cache    8.80%
# class LRUCache:
#     def __init__(self, capacity: int):
#         self.cache = {}
#         self.used = []
#         self.capacity = capacity
#
#     def get(self, key: int) -> int:
#         if key in self.cache:
#             self.used.remove(key)
#             self.used.append(key)
#             return self.cache[key]
#         else:
#             return -1
#
#     def put(self, key: int, value: int) -> None:
#         if key in self.cache:
#             self.used.remove(key)
#             self.used.append(key)
#             self.cache[key] = value
#         else:
#             self.cache[key] = value
#             self.used.append(key)
#             if len(self.used) > self.capacity:
#                 lru = self.used.pop(0)
#                 del(self.cache[lru])

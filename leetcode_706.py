# Design HashMap

class LinkedNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.root = None

    def ifexists(self, key):
        if self.root is None:
            return False
        head = self.root
        while head:
            if head.key == key:
                return True
            head = head.next
        return False

    def insertOrUpdate(self, key, value):
        if self.root is None:
            node = LinkedNode(key, value)
            self.root = node
            return self.root
        head = self.root
        if self.ifexists(key):
            while head:
                if head.key == key:
                    head.value = value
                    break
                else:
                    head = head.next
        else:
            while head:
                if head.next is None:
                    node = LinkedNode(key, value)
                    head.next = node
                    break
                head = head.next
        return self.root

    def delete(self, key):
        head = self.root
        if head.key == key:
            self.root = head.next
        else:
            while head.next:
                if head.next.key == key:
                    head.next = head.next.next
                    break
                else:
                    head = head.next


class MyHashMap:

    def __init__(self):
        self.hashmap = [None]*10**3

    def put(self, key: int, value: int) -> None:
        indx = key % 10**3
        if self.hashmap[indx] is None:
            ll = LinkedList()
        else:
            ll = self.hashmap[indx]
        ll.insertOrUpdate(key, value)
        self.hashmap[indx] = ll

    def get(self, key: int) -> int:
        indx = key % 10 ** 3
        if self.hashmap[indx] is None:
            return -1
        else:
            ll = self.hashmap[indx]
            if not ll.ifexists(key):
                return -1
            else:
                head = ll.root
                while head:
                    if head.key == key:
                        return head.value
                    else:
                        head = head.next

    def remove(self, key: int) -> None:
        indx = key % 10 ** 3
        if self.hashmap[indx] is None:
            pass
        else:
            head = self.hashmap[indx]
            if head.ifexists(key):
                head.delete(key)



        # Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)

obj = MyHashMap()
obj.put(1, 1)
obj.put(2, 2)
print(obj.get(1))
print(obj.get(2))

obj.put(2, 3)
print(obj.get(2))

obj.put(1002, 1002)
obj.put(2002, 2002)
obj.put(3002, 3002)
print(obj.get(3002))
print(obj.get(2002))
print(obj.get(4002))

obj.remove(2)
print(obj.get(2))
obj.remove(4002)
obj.remove(3002)
obj.remove(2003)


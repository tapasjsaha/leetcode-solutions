# Design Linked List
class LinkNode:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next

class MyLinkedList:
    def __init__(self):
        self.head = None

    def get(self, index: int) -> int:
        root = self.head
        current_index = 0
        while root and current_index < index:
            current_index += 1
            root = root.next
        if root and current_index == index:
            return root.val
        else:
            return -1

    def addAtHead(self, val: int) -> None:
        node = LinkNode(val, self.head)
        self.head = node

    def addAtTail(self, val: int) -> None:
        node = LinkNode(val)
        if self.head is None:
            self.head = node
        else:
            root = self.head
            while root.next:
                root = root.next
            root.next = node

    def addAtIndex(self, index: int, val: int) -> None:
        if index == 0:
            self.addAtHead(val)
        else:
            root = self.head
            current_index = 0
            while root and current_index < index-1:
                current_index += 1
                root = root.next
            if current_index == index-1 and root:
                node = LinkNode(val, root.next)
                root.next = node

    def deleteAtIndex(self, index: int) -> None:
        if index == 0:
            if self.head is not None:
                self.head = self.head.next
        else:
            root = self.head
            current_index = 0
            while root and current_index < index-1:
                current_index += 1
                root = root.next
            if current_index == index-1 and root and root.next is not None:
                root.next = root.next.next

    # Not part of the problem :
    def printList(self):
        root = self.head
        while root:
            print(str(root.val) + '-->', end='')
            root = root.next
        print('')


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)

# Test case 4
obj3 = MyLinkedList()
obj3.addAtHead(1)
obj3.addAtTail(2)
obj3.addAtIndex(3,2)
obj3.printList()

# Test case 3
obj2 = MyLinkedList()
obj2.addAtHead(1)
obj2.addAtTail(2)
obj2.addAtIndex(1, 2)
obj2.printList()
print(obj2.get(1))
obj2.deleteAtIndex(1)
obj2.printList()
print(obj2.get(1))
print(obj2.get(3))
obj2.deleteAtIndex(3)
obj2.printList()
obj2.deleteAtIndex(0)
obj2.printList()
print(obj2.get(0))
obj2.deleteAtIndex(0)
obj2.printList()
print(obj2.get(0))

#Test case 1


obj = MyLinkedList()
obj.printList()
obj.addAtHead(4)
obj.printList()
obj.addAtHead(2)
obj.printList()
obj.addAtTail(5)
obj.printList()
obj.addAtIndex(0, 1)
obj.printList()
obj.addAtIndex(2, 3)
obj.printList()
print(obj.get(0))
print(obj.get(1))
print(obj.get(2))
print(obj.get(3))
print(obj.get(4))
print(obj.get(5))
print(obj.get(6))
print("---------------")
obj.printList()
obj.deleteAtIndex(4)
obj.printList()
obj.deleteAtIndex(1)
obj.printList()
obj.deleteAtIndex(7)
obj.printList()
obj.deleteAtIndex(0)
obj.printList()
print("---------------")

obj1 = MyLinkedList()
obj1.addAtTail(3)
obj1.printList()
obj1.addAtTail(4)
obj1.printList()
obj1.addAtIndex(4, 5)
obj1.printList()
obj1.addAtIndex(2, 5)
obj1.printList()
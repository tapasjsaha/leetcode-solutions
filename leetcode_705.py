# Design HashSet
class MyHashSet:
    def __init__(self):
        self.bucket = 1000
        self.hashset = [[] for _ in range(self.bucket)]

    def add(self, key: int) -> None:
        if self.contains(key):
            pass
        else:
            keyval = key % self.bucket
            self.hashset[keyval].append(key)

    def remove(self, key: int) -> None:
        if self.contains(key):
            keyval = key % self.bucket
            self.hashset[keyval].remove(key)

    def contains(self, key: int) -> bool:
        keyval = key % self.bucket
        if key in self.hashset[keyval]:
            return True
        else:
            return False

# Your MyHashSet object will be instantiated and called as such:
obj = MyHashSet()
obj.add(1)
obj.add(2)
print(obj.contains(1))
print(obj.contains(3))
obj.add(2)
print(obj.contains(2))
obj.remove(2)
print(obj.contains(2))

# param_3 = obj.contains(key)
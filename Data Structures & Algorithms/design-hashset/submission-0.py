class MyHashSet:

    def __init__(self):
        self.s=[]

    def add(self, key: int) -> None:
        for e in self.s:
            if e==key: return
        self.s.append(key)
        return

    def remove(self, key: int) -> None:
        for e in self.s:
            if e==key: 
                self.s.remove(key)
                return
        return

    def contains(self, key: int) -> bool:
        for e in self.s:
            if e==key: return True
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
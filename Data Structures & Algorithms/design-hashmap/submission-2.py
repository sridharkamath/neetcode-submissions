class MyHashMap:

    def __init__(self):
        self.hashtable=[-1]*1000000
        self.hashfunc= lambda x: x%1000000

    def put(self, key: int, value: int) -> None:
        self.hashtable[self.hashfunc(key)]=value

    def get(self, key: int) -> int:
        value=self.hashtable[self.hashfunc(key)]
        return value

    def remove(self, key: int) -> None:
        self.hashtable[self.hashfunc(key)]=-1
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
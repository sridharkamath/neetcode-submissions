class TimeMap:

    def __init__(self):
        self.kv_store=defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.kv_store[key].append((timestamp,value))

    def get(self, key: str, timestamp: int) -> str:
        arr=self.kv_store[key]
        if len(arr)==0:
            return ""
        l,r=0,len(arr)-1
        ans=""
        while l<=r:
            mid=(l+r)//2
            print(arr[mid],arr[mid][0],arr[mid][1])
            if arr[mid][0]<timestamp:
                ans=arr[mid][1]
                l=mid+1
            elif arr[mid][0]>timestamp:
                r=mid-1
            elif arr[mid][0]==timestamp:
                return arr[mid][1]
        return ans if ans else ""

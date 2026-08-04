class MedianFinder:

    def __init__(self):
        self.minheap = []
        self.maxheap = []

    def addNum(self, num: int) -> None:
        if self.minheap and num>=self.minheap[0]:
            heapq.heappush(self.minheap,num)
        else:
            heapq.heappush(self.maxheap,-1*num)
        
        if len(self.maxheap) > len(self.minheap) + 1:
            heapq.heappush(self.minheap, -heapq.heappop(self.maxheap))

        if len(self.minheap) > len(self.maxheap):
            heapq.heappush(self.maxheap, -heapq.heappop(self.minheap))




    def findMedian(self) -> float:
        if len(self.minheap)>len(self.maxheap):
            return self.minheap[0]
        elif len(self.minheap)<len(self.maxheap):
            return -1*self.maxheap[0]
        else:
            return (self.minheap[0]-self.maxheap[0])/2
        
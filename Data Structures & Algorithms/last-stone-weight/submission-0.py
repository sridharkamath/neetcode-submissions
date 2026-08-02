class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for s in stones:
            heapq.heappush(heap,-s)
        while len(heap)>1:
            x = -1*heapq.heappop(heap)
            y = -1*heapq.heappop(heap)
            if x==y:
                continue
            else:
                heapq.heappush(heap,-1*abs(x-y))
        return -1*heap[0] if heap else 0
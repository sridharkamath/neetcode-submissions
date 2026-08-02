from collections import Counter, deque
import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks)

        h = [-f for f in freq.values()]
        heapq.heapify(h)

        q = deque()

        time = 0

        while h or q:
            time += 1

            if h:
                cnt = 1 + heapq.heappop(h)

                if cnt:
                    q.append((time + n, cnt))

            if q and q[0][0] == time:
                _, cnt = q.popleft()
                heapq.heappush(h, cnt)

        return time
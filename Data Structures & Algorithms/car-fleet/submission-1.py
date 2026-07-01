class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        s=[]
        for x,v in sorted(zip(position,speed), reverse=True):
            time=(target-x)/v
            if not s:
                s.append(time)
            else:
                curr_max_slow_time=s[-1]
                if time>curr_max_slow_time:
                    s.append(time)
        return len(s)

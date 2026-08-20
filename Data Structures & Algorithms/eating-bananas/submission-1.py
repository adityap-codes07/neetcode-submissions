import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lb = 1
        ub = max(piles)
        ans = ub
        while lb <= ub:
            mid = (lb + ub) // 2
            time = 0
            for i in piles:
                time += math.ceil(i/mid)
            if time <= h:
                ans = mid 
                ub = mid - 1
            else:
                lb = mid + 1
        return ans
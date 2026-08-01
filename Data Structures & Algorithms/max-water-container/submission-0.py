class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxWater = 0
        n = len(heights)
        l = 0
        r = n - 1
        while l < r:
            width = r - l
            currLevel = width * min(heights[l], heights[r])
            maxWater = max(maxWater, currLevel)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return maxWater

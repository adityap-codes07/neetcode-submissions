class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        nums = list(set(nums))
        nums.sort()
        c = mc = 1
        p1, p2 = 0, 1
        while p2 < len(nums):
            if nums[p1] + 1 == nums[p2]:
                c += 1
                mc = max(mc, c)
            else:
                c = 1
            p1 += 1
            p2 += 1
        return mc

            


        
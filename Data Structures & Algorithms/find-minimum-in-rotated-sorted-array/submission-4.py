class Solution:
    def findMin(self, nums: List[int]) -> int:
        lb = 0
        ub = len(nums) - 1
        ans = nums[0] 
        while lb <= ub:
            if nums[lb] < nums[ub]:
                ans = min(ans, nums[lb])
                break
            m = (lb + ub) // 2
            ans = min(ans, nums[m])
            if nums[m] >= nums[lb]:
                lb = m + 1
            else:
                ub = m - 1
        return ans
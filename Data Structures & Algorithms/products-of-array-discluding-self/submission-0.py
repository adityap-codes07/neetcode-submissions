class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = []
        for i in range(len(nums)):
            ele = 1
            for j in range(len(nums)):
                if i == j:
                    continue
                else:
                    ele *= nums[j]
            prod.append(ele)
        return prod


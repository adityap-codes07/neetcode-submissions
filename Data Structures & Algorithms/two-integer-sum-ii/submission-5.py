class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        lb, ub = 0, n - 1
        while lb < ub:
            if numbers[lb] + numbers[ub] == target:
                return [lb + 1, ub + 1]
            elif numbers[lb] + numbers[ub] > target:
                ub -= 1
            else:
                lb += 1
        return []
            
        
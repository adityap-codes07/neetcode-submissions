class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        for i in range(n):
            need = target - numbers[i]
            lb = i + 1
            ub = n - 1
            while lb <= ub:
                mid = (lb + ub) // 2
                if numbers[mid] == need:
                    return ([i + 1, mid + 1])
                elif numbers[mid] > need:
                    ub = mid - 1
                else:
                    lb = mid + 1
        return []
        
        
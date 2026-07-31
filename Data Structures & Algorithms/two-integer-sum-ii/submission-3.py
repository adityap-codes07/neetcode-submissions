class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        flag = False
        idx1 = 0
        idx2 = 0
        
        for i in range(n):
            idx1 = i
            need = target - numbers[i]
            lb = i + 1
            ub = n - 1
            while lb <= ub:
                mid = (lb + ub) // 2
                if numbers[mid] == need:
                    idx2 = mid
                    flag = True
                    break
                elif numbers[mid] > need:
                    ub = mid - 1
                else:
                    lb = mid + 1
            if flag:
                break
        return ([idx1 + 1, idx2 + 1])
        
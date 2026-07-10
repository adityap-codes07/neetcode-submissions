class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix)
        top = 0
        bottom = n - 1
        row = -1
        while top <= bottom:
            mid = (top + bottom) // 2
            if target < matrix[mid][0]:
                bottom = mid - 1
            elif target > matrix[mid][-1]:
                top = mid + 1
            else:
                row = mid
                break
        i = 0
        j = len(matrix[0]) - 1
        while i <= j:
            mid = (i + j) // 2
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] > target:
                j = mid - 1
            else:
                i = mid + 1
        return False

        
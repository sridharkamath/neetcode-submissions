class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0]) if rows > 0 else 0

        l = 0
        r = rows * cols - 1

        while l <= r:
            mid = l + (( r - l ) // 2)

            mid_col = mid % cols
            mid_row =  mid // cols

            val = matrix[mid_row][mid_col]

            if val > target:
                r = mid - 1
            elif val < target:
                l = mid + 1
            else:
                return True
        
        return False
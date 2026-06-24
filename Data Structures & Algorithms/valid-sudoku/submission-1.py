class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        row_nums = [[0]*9 for _ in range(9)]
        col_nums = [[0]*9 for _ in range(9)]
        box_nums = [[[0]*9 for _ in range(3)] for _ in range(3)]

        for i in range(9):
            for j in range(9):
                num=board[i][j]
                if num==".":
                    continue
                elif row_nums[i][int(num)-1] or col_nums[j][int(num)-1] or box_nums[i//3][j//3][int(num)-1]:
                    return False
                row_nums[i][int(num)-1]^=1
                col_nums[j][int(num)-1]^=1
                box_nums[i//3][j//3][int(num)-1]^=1

        return True
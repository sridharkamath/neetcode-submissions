class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        row=[1]
        for i in range(1,rowIndex+1):
            next_val=row[-1]*(rowIndex+1-i)//i
            row.append(next_val)
        return row
from typing import List


class Solution:
    
    
    
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        collectionSet: set = set()
        # Validate the rows
        for row in board:
            collectionSet.clear()
            for item in row:
                if (item == "."):
                    continue
                if (item in collectionSet):
                    return False
                collectionSet.add(item)
        
        collectionSet.clear()
        # Validate the columns
        for itemIndex in range(len(board[0])): # All board rows are the same length, so just take the 0th index.
            collectionSet.clear()
            for row in board:
                if row[itemIndex] == ".":
                    continue
                if row[itemIndex] in collectionSet:
                    return False
                collectionSet.add(row[itemIndex])
        
        collectionSet.clear()
        # Validate each square
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                if not self.squareValidation(board, i, i + 3, j, j + 3):
                    return False
        
        # All checks passed
        return True
    
    def squareValidation(self, board: List[List[str]], rowLower: int, rowHigher: int, columnLower: int, columnHigher: int) -> bool:
            collectionSet: set = set()
            for row in board[rowLower:rowHigher]:
                for item in row[columnLower:columnHigher]:
                    if (item == "."):
                        continue
                    if (item in collectionSet):
                        return False
                    collectionSet.add(item)
            return True

solution = Solution()

board = [["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

print(solution.isValidSudoku(board))
    
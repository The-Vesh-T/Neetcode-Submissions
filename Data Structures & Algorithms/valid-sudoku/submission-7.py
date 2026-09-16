class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #check each row (9 rows)
        for row in range(9):
            #make a set add num to it
            seen = set()
            #Check each val in row then add to set if no exist
            for i in range(9):
                if board[row][i] == ".":
                    continue
                if board[row][i] in seen:
                    return False
                seen.add(board[row][i])
        
        #check each col
        for col in range(9):
            seen = set()
            for i in range(9):
                if board[i][col] == '.':
                    continue
                if board[i][col] in seen:
                    return False
                seen.add(board[i][col])

        #now squares check 3 then next 3
        for square in range(9):
            seen = set()
            for i in range(3):
                for j in range(3):
                    row = (square//3)*3+i
                    col = (square%3)*3+j
                    if board[row][col] == '.':
                        continue
                    if board[row][col] in seen:
                        return False
                    seen.add(board[row][col])
        return True

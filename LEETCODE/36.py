class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        m = len(board)
        n = len(board[0])
        # if it is not 9 X 9
        if m != 9 or n != 9:
            return -1
        # check 1-9 appears once and only once in every row
        for i in range(m):
            validRow = [False] * m
            for j in range(n):
                if (board[i][j] == "."): continue
                elif validRow[int(board[i][j])-1] == True:
                    return False
                else:
                    validRow[int(board[i][j])-1] = True
        # check 1-9 appears once and only once in every column
        for i in range(m):
            validCol = [False] * m
            for row in board:
                if row[i] == ".": continue
                elif validCol[int(row[i])-1] == True:
                    return False
                else:
                    validCol[int(row[i])-1] = True
        # check every 3x3 sub matrix appears 1-9 once and only once
        for box in range(m):
            valid = [False] * m
            for row in range(3):
                for col in range(3):
                    ele = board[row+ 3* (box//3)][col + 3 * (box%3)]
                    if ele == ".": continue
                    elif valid[int(ele)-1] == True: return False
                    else: valid[int(ele)-1] = True
        return True
board = [["8","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
print(Solution().isValidSudoku(board))
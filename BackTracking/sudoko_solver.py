class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        def isValid(board,row,col,element):
            # First checking the rows
            for i in range(0,9):
                if board[row][i] == element:
                    return False
                
            # Now checking the col
            for i in range(0,9):
                if board[i][col] == element:
                    return False
                
            # Now I have to check the Grids
            tempRow= 3 * (row // 3)
            tempCol= 3 * (col // 3)

            for i in range(3):
                for j in range(3):
                    if board[tempRow+i][tempCol+j] == element:
                        return False
                
            return True

        def sudokuSolver(board,row,col):
            # Base Case conditions
            if row == 9: return True

            # if Column is at last position then we reset the col to 0 & increment the row
            if col == 9: return sudokuSolver(board,row+1,0) 

            # if the position is not empty then we have to check for the next position
            if board[row][col] != '.' : return sudokuSolver(board,row,col+1)

            # now we have to iterate through choices
            for i in map(str, range(1, 10)):
                # validating the choice
                if isValid(board,row,col,i):
                    # making the choice
                    board[row][col]=str(i)
                    # recursion 
                    if sudokuSolver(board,row,col+1) : return True
                    # REverting the choice
                    board[row][col]='.'

            # if all the conditions don't work
            return False
    
        sudokuSolver(board,0,0)

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        #Number of rows and columns 

        ROWS, COLS = len(board), len(board[0]) 

        rows = defaultdict(set) #for rows

        cols = defaultdict(set) #for cols 

        squares = defaultdict(set) #for r, c 

        for r in range(ROWS) : 

            for c in range(COLS) : 

                if board[r][c] == "." : 

                    continue 

                if (board[r][c] in rows[r] 
                
                    or board[r][c] in cols[c] 
                    
                    or board[r][c] in squares[(r // 3, c // 3)]) : 

                    return False 

                #Add the elements inside 

                cols[c].add(board[r][c])
                
                rows[r].add(board[r][c])

                squares[(r // 3, c // 3)].add(board[r][c]) 

        return True 

                


        
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        #Find the rows and cols of the matrix 

        ROWS, COLS = len(matrix), len(matrix[0])

        top, bottom = 0, ROWS - 1 #Top and bottom of the row 

        #Perform a binary 

        while top <= bottom : 

            row = (top + bottom) // 2

            #If the target > first element of the row 

            if target > matrix[row][-1] : 

                top = row + 1 

            elif target < matrix[row][0] : 

                bottom = row - 1 

            #If target found, it's in the row 

            else : 

                break 

            #If no valid row ==> return false 

        if not (top <= bottom) : 

            return False 

            #Perform binary search on cols 

        rows = (top + bottom) // 2 

        l, r = 0, COLS - 1 

        while l <= r : 

            m = (l + r) // 2 

            if target > matrix[row][m] : 

                l = m + 1 

            elif target < matrix[row][m] : 

                r = m - 1 

            else : 

                return True 

        return False 
        
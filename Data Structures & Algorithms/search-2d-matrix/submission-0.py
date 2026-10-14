class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        rows , cols = len(matrix), len(matrix[0]) 

        top, bottom = 0, rows - 1 

        while top <= bottom : 

            current_row = (top + bottom )// 2 

            if target > matrix[current_row][-1] : 

                top = current_row + 1 

            elif target < matrix[current_row][0] : 

                bottom = current_row - 1 

            else : 

                break 

        if not (top <= bottom) : 

            return False 

        current_row = (top + bottom) // 2 

        head, tails = 0 , cols - 1 

        while head <= tails : 

            middle = (head + tails )// 2  

            if target > matrix[current_row][middle] : 

                head = middle + 1 

            elif target < matrix[current_row][middle] : 

                tails = middle - 1 

            else : 

                return True 

        return False  

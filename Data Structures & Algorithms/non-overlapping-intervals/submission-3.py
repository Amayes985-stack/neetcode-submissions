class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:


        #First thing first, we'd sort the intervals by pairs 

        intervals.sort(key = lambda pair: pair[1]) 

        #We keep track of the previous end of the interval 
        prevEnd = intervals[0][1]

        #We have a result variable to keep track 
        result = 0 

        #As we iterate through the array, if the previous end is greater than 
        #the other start of the interval, -> non-overlapping interval 

        for i in range(1, len(intervals)) : 

            if prevEnd > intervals[i][0] : 

                result += 1 

            else: 

                prevEnd = intervals[i][1] 


        return result 



        

        

        
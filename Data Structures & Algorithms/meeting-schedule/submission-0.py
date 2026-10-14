"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:

        intervals.sort(key=lambda i: i.start) 

        #First thing first, we sort the intervals by start date 


        for i in range(1, len(intervals)) : 

            #As we iterate through the problem, we keep track of the intervals 

            i1 = intervals[i - 1] 

            i2 = intervals[i] 

            #We check if the enfing date of the first meeting overlaps wth the b
            #Beginning of the other one, if tha's the case, then it's a no 

            if i1.end > i2.start : 

                return False 

        #Otherwise, we'd return True 

        return True 


        #Time complexity : O(n*log(n))

        #Space complexity : O(n) or O(1) depending on the sorting algorithm  

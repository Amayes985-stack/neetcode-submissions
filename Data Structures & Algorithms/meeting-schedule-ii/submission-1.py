"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:

        intervals.sort(key=lambda x: x.start)

        min_heap = [] #Using a heap 

        for interval in intervals : 

            #For every interval, if my min_heap is not empty and the top of my heap 

            #is less than the interval start , meaning that we finished it 

            #We pop, the element, otherwise, we'd push the interval within the heap 

            if min_heap and min_heap[0] <= interval.start : 

                heapq.heappop(min_heap) 

            heapq.heappush(min_heap, interval.end) 


        return len(min_heap) 


        
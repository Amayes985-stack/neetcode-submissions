class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:

        intervals.sort() 

        min_heap = []

        result, index  = {}, 0

        for q in sorted(queries) :  

            while index < len(intervals) and intervals[index][0] <= q : 

                l, r = intervals[index] 

                heapq.heappush(min_heap, (r - l + 1, r)) 

                index += 1 

            while min_heap and min_heap[0][1] < q : 

                heapq.heappop(min_heap) 

            result[q] = min_heap[0][0] if min_heap else -1 

        return [result[q] for q in queries]
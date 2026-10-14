class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        #each task 1 unit of time 

        #Minium idle time 

        count = Counter(tasks)

        maxHeap = [-cnt for cnt in count.values()] 

        heapq.heapify(maxHeap) 

        #Keep track of time 

        time = 0 

        q = deque() #Pairs of [-cnt, time] 

        while maxHeap or q : 

            time += 1 

            if maxHeap : 

                cnt = 1 + heapq.heappop(maxHeap)  

                if cnt : 

                    q.append([cnt, time + n]) 


            if q and q[0][1] == time : 

                heapq.heappush(maxHeap, q.popleft()[0]) 

        return time 
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        head, tails = 0, len(numbers) - 1 

        while head < tails : 

            if numbers[head] + numbers[tails] > target : 

                tails -= 1 

            elif numbers[head] + numbers[tails] < target : 

                head += 1 

            else : 

                return [head + 1 , tails + 1 ]


        return []
        
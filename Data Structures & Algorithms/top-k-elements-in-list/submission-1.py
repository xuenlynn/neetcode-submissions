class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Method 1 (with DS): iterate through array and get frequency count of each number and store in hash map-> maintain a min-heap of size k -> only if the count of a number exceeds the root minimum, then it can be added to heap -> up-head bubbling may be required

        # Method 2 (without DS): iterate through array and get frequency count of each number and store in hash map -> initialise empty array and iterate through hash map and create tuple (count, number) -> create array of tuples and pop the top k 

        # Learnings: NOT max-heap because size of heap may be more than k + extraction for k times. Min-heap maintains size of k at all times

        # Method 2
        num_count = {}
        for num in nums:
            num_count[num] = 1 + num_count.get(num, 0)
            # find value of key and +1
        
        num_count_list= []
        for num, count in num_count.items():
            num_count_list.append((count, num))
        num_count_list.sort()

        result = []
        while len(result) < k:
            result.append(num_count_list.pop()[1])
        return result
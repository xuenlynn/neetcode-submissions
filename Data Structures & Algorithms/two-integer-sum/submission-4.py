class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
    # target - number to find other number
    # if the other number exists, return the index
    # iterate through array as i -> target - i, then check whether other number is in array -> return index
        result = []
        for index, num in enumerate(nums):
            other = target - num
            if other in nums and nums.index(other)!= index:
                result.append(index)
                result.append(nums.index(other))
                result.sort()
                return result

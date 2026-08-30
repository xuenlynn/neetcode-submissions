class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # target - number to find other number
        # if the other number exists, return the index
        # enumerate the array -> find the complement -> if the complement exists and its index isn't the same as the current number, append to result array -> sort the array in asc.
        # result = []
        # for index, num in enumerate(nums):
        #     other = target - num
        #     if other in nums and nums.index(other)!= index:
        #         result.append(index)
        #         result.append(nums.index(other))
        #         result.sort()
        #         return result

        # 2 hash maps method: 1 maps each number to its index, another to find the complement
        indices = {}
        for index, number in enumerate(nums):
            indices[number] = index

        for index, number in enumerate(nums):
            other = target - number
            if other in indices and indices[other] != index:
                return [index, indices[other]]


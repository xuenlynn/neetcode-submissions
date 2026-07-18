class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 2:
            return [0,1]
        # brute force, O(n^2)
        # range can actually be len(nums) - 1, since last number would have already been paired up with all earlier numbers
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        
        # O(n) mathematical equation, target - nums[i] = nums[j]
        # for i in range(len(nums)):
        #     num2 = target - nums[i]
        #     if num2 in nums and nums[i] == num2:

                
                




            
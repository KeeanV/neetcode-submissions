class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_map = {}
        for i in range(len(nums)):
            my_map[nums[i]] = i
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in my_map and i != my_map[complement]:
                return [i,my_map[complement]]
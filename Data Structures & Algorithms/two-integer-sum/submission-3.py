class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_map = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement not in my_map:
                my_map[nums[i]] = i
            else:
                return [my_map[complement], i]
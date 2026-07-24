class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        sorted_copy = sorted(nums)
        for i in range(1,len(sorted_copy)):
            if sorted_copy[i] == sorted_copy[i-1]:
                return True
        return False
         


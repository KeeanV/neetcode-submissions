class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        my_map = {}
        for i in nums:
            if i not in my_map:
                my_map[i] = 0
            my_map[i] +=1
            if my_map[i] > 1:
                return True
        return False

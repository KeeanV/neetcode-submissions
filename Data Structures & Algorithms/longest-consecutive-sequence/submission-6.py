class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
       my_set = set(nums)
       longest = 0
       for i in my_set:
        if i-1 not in my_set:
            streak = 1
            curr = i
            while curr+1 in my_set:
                curr+=1
                streak+=1
            longest = max(longest, streak)
       return longest